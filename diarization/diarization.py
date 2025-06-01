from pyannote.audio import Pipeline
import matplotlib.pyplot as plt
from pyannote.core import Segment
import matplotlib.patches as mpatches
import csv,os
from dotenv import load_dotenv



load_dotenv() 

def diarize_local(audio_file):
    token = os.getenv("HUGGINGFACE_HUB_TOKEN")
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization@2.1", use_auth_token=token)
    diarization = pipeline(audio_file)

    print(diarization)

    with open("output.rttm", "w") as rttm:
        diarization.write_rttm(rttm)

    save_diarization_to_csv(diarization, "output_diarization.csv")
    plot_diarization(diarization, "output_diarization.png")
    

def save_diarization_to_csv(diarization, output_csv_path="diarization.csv"):
    """
    Save diarization result to CSV with columns: start_time, end_time, speaker_label
    """
    with open(output_csv_path, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["start_time", "end_time", "speaker_label"])

        for turn, _, speaker in diarization.itertracks(yield_label=True):
            writer.writerow([f"{turn.start:.2f}", f"{turn.end:.2f}", speaker])

    print(f"Saved diarization output to {output_csv_path}")


def plot_diarization(diarization, output_image="diarization_plot.png"):
    fig, ax = plt.subplots(figsize=(10, 3))

    speakers = list(set(label for _, _, label in diarization.itertracks(yield_label=True)))
    speakers.sort()
    color_map = {speaker: f"C{i}" for i, speaker in enumerate(speakers)}

    for turn, _, speaker in diarization.itertracks(yield_label=True):
        ax.plot([turn.start, turn.end], [speaker, speaker], lw=6, color=color_map[speaker], solid_capstyle='butt')

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Speaker")
    ax.set_title("Speaker Diarization Timeline")
    ax.grid(True)

    # Optional: Create a legend
    legend_patches = [mpatches.Patch(color=color_map[s], label=s) for s in speakers]
    ax.legend(handles=legend_patches, loc="upper right")

    plt.tight_layout()
    plt.savefig(output_image)
    print(f"Saved diarization plot to {output_image}")
    plt.show()