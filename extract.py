import os
import shutil
import glob

# Base path where your MemoTag project lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "Data")

# Target folders to store wavs
healthy_wav_dir = os.path.join(BASE_DIR, "healthy_wav")
patient_wav_dir = os.path.join(BASE_DIR, "patient_wav")

print(f"Working with directories:\nBase: {BASE_DIR}\nData: {DATA_DIR}\nHealthy output: {healthy_wav_dir}\nPatient output: {patient_wav_dir}\n")

# Create the output folders if they don't exist
os.makedirs(healthy_wav_dir, exist_ok=True)
os.makedirs(patient_wav_dir, exist_ok=True)

def collect_and_copy_wavs(source_root, destination_root, group_name):
    if not os.path.exists(source_root):
        print(f"Error: Source directory {source_root} does not exist!")
        return

    total_copied = 0
    print(f"\nProcessing {group_name} data from {source_root}")

    for participant in os.listdir(source_root):
        participant_path = os.path.join(source_root, participant)

        if not os.path.isdir(participant_path):
            continue  # Skip any non-folder files

        print(f"Processing participant: {participant}")
        for session in os.listdir(participant_path):
            session_path = os.path.join(participant_path, session)

            if not os.path.isdir(session_path):
                continue

            wav_files = glob.glob(os.path.join(session_path, "*.wav"))
            for wav in wav_files:
                try:
                    filename = f"{participant}_{session}_{os.path.basename(wav)}"
                    destination = os.path.join(destination_root, filename)
                    shutil.copy2(wav, destination)
                    total_copied += 1
                    print(f"Copied: {filename}")
                except Exception as e:
                    print(f"Error copying {wav}: {str(e)}")
    
    return total_copied

try:
    # Collect and copy for Healthy
    healthy_count = collect_and_copy_wavs(os.path.join(DATA_DIR, "Healthy"), healthy_wav_dir, "Healthy")

    # Collect and copy for Patients
    patient_count = collect_and_copy_wavs(os.path.join(DATA_DIR, "Patients"), patient_wav_dir, "Patients")

    print(f"\n✅ Done! Copied {healthy_count} healthy wav files and {patient_count} patient wav files.")
except Exception as e:
    print(f"❌ An error occurred: {str(e)}")
