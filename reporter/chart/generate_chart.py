#  type: ignore

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as patches
import matplotlib.lines as mlines
from PIL import Image, ImageOps
import sys
import os

# Constants for logo name and custom font
LOGO_NAME = "qaband.com"
pathfile = os.path.abspath("./reporter/chart/font.ttf")
CUSTOM_FONT = fm.FontProperties(fname=pathfile)


# Function to create legend elements
def create_legend_elements(data):
    return [
        mlines.Line2D(
            [0],
            [0],
            color=d["color"],
            marker=".",
            linestyle="None",
            markeredgecolor=d["color"],
            markersize=8,
            markeredgewidth=1.2,
        )
        for d in data
        if d["value"] > 0
    ]


# Function to apply custom font to legend
def apply_custom_font_to_legend(legend):
    for text in legend.get_texts():
        text.set_fontproperties(CUSTOM_FONT)
        text.set_fontsize(9)


# Function to generate chart
def generate_chart(total, passed, failed, broken, skipped, sum_duration):
    data = [
        {
            "label": "Passed",
            "value": passed,
            "color": (0 / 255, 128 / 255, 0 / 255, 0.5),
        },
        {
            "label": "Failed",
            "value": failed,
            "color": (255 / 255, 99 / 255, 132 / 255, 0.7),
        },
        {
            "label": "Broken",
            "value": broken,
            "color": (255 / 255, 159 / 255, 64 / 255, 0.6),
        },
        {
            "label": "Skipped",
            "value": skipped,
            "color": (255 / 255, 205 / 255, 86 / 255, 0.6),
        },
    ]

    # Labels, sizes and colors for the chart
    labels = [d["label"] + f": {d['value']}" for d in data if d["value"] > 0]
    sizes = [d["value"] for d in data if d["value"] > 0]
    colors = [d["color"] for d in data if d["value"] > 0]

    # Create the plot
    fig, ax = plt.subplots(figsize=(6.4 * 0.83, 4.8 * 0.83))
    wedges, texts, autotexts = ax.pie(
        sizes,
        colors=colors,
        startangle=90,
        autopct="%1.2f%%",
        textprops={
            "color": "black",
            "bbox": dict(
                facecolor="white",
                edgecolor=(169 / 255, 169 / 255, 169 / 255, 0.5),
                boxstyle="round,pad=0.5",
            ),
        },
    )

    # Change the font size
    plt.setp(autotexts, size=6)

    # Set the title
    plt.title("Test Results", fontproperties=CUSTOM_FONT, fontsize=12, color="black")

    # Move the plot to the left
    fig.subplots_adjust(left=0.1, right=0.76)

    # Create legend
    legend_elements = create_legend_elements(data)
    legend = ax.legend(
        legend_elements,
        labels,
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
        handlelength=1,
        handletextpad=0.4,
    )

    # Apply custom font to legend text
    apply_custom_font_to_legend(legend)

    # Draw a white circle at the center
    centre_circle = plt.Circle((0, 0), 0.70, fc="white")
    ax.add_artist(centre_circle)

    # Set the edge color of the legend frame
    legend.get_frame().set_edgecolor((169 / 255, 169 / 255, 169 / 255, 0.5))

    # Create a fancy box with rounded corners
    fancy_box1 = patches.FancyBboxPatch(
        (-1.1, -1.1),
        2.2,
        2.2,
        boxstyle="round,pad=0.02",
        linewidth=1,
        edgecolor=(169 / 255, 169 / 255, 169 / 255, 0.3),
        facecolor="none",
        zorder=-1,
    )
    fancy_box2 = patches.FancyBboxPatch(
        (-1.05, -1.05),
        2.1,
        2.1,
        boxstyle="round,pad=0.02",
        linewidth=1,
        edgecolor=(169 / 255, 169 / 255, 169 / 255, 0.6),
        facecolor="none",
        zorder=-1,
    )

    # Add the fancy boxes to the plot
    ax.add_patch(fancy_box1)
    ax.add_patch(fancy_box2)

    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.axis("equal")

    # Add text 'Total' in center with a box around it
    plt.text(
        0,
        0.02,
        f"Total: {total}",
        horizontalalignment="center",
        verticalalignment="center",
        fontsize=11,
        color="black",
        fontproperties=CUSTOM_FONT,
        bbox=dict(
            facecolor="white",
            edgecolor=(169 / 255, 169 / 255, 169 / 255, 0.5),
            boxstyle="round,pad=0.5",
        ),
    )

    # Add text 'duration' with a smaller font size and a box around it
    minutes, seconds = divmod(
        int(sum_duration) / 1000, 60
    )  # Convert from milliseconds to seconds
    plt.text(
        0,
        -0.21,
        f"{int(minutes)}min {int(seconds)}sec",
        horizontalalignment="center",
        verticalalignment="center",
        fontsize=6.5,
        color="gray",
        fontproperties=CUSTOM_FONT,
        bbox=dict(
            facecolor="white",
            edgecolor=(169 / 255, 169 / 255, 169 / 255, 0.5),
            boxstyle="round,pad=0.5",
        ),
    )

    # Add the text "logo_name" to the up of the legend
    plt.text(
        1.82,
        0.6,
        LOGO_NAME,
        horizontalalignment="center",
        verticalalignment="center",
        fontsize=11.5,
        color="black",
        fontproperties=CUSTOM_FONT,
    )

    # Save the plot
    plt.savefig("chart.png", dpi=300, bbox_inches="tight", pad_inches=0.1)

    # Open the saved image
    img = Image.open("chart.png")
    # If the image is not RGBA, convert it
    if img.mode != "RGBA":
        img = img.convert("RGBA")

    # Add padding
    padding = (20, 20, 20, 20)  # Change these values to adjust the padding size
    img_with_padding = ImageOps.expand(img, border=padding, fill="white")

    # Save the result back to the same file
    img_with_padding.save("chart.png")


# Main function to generate chart
if __name__ == "__main__":
    total = int(os.getenv("TOTAL"))
    passed = int(os.getenv("PASSED"))
    failed = int(os.getenv("FAILED"))
    broken = int(os.getenv("BROKEN"))
    skipped = int(os.getenv("SKIPPED"))
    sum_duration = int(os.getenv("SUMDURATION"))

    generate_chart(total, passed, failed, broken, skipped, sum_duration)
