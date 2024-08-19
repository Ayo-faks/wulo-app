import os
import shutil

# Define the source and destination directories
SOURCE_DIR = "/workspaces/wulo-graph-index/ragtest/output/20240814-195240/artifacts"  # Adjust this to the actual path of your indexing pipeline output
DEST_DIR = "/workspaces/wulo-graph-index/ragtest/inputs/operation dulce"

# List of files to transfer, based on the code analysis
FILES_TO_TRANSFER = [
    "create_final_community_reports.parquet",
    "create_final_nodes.parquet",
    "create_final_entities.parquet",
    "create_final_relationships.parquet",
    "create_final_covariates.parquet",
    "create_final_text_units.parquet"
]

def transfer_files():
    # Create the destination directory if it doesn't exist
    os.makedirs(DEST_DIR, exist_ok=True)
    
    # Create the LanceDB directory
    os.makedirs(os.path.join(DEST_DIR, "lancedb"), exist_ok=True)
    
    # Counter for transferred files
    transferred_count = 0
    
    for file in FILES_TO_TRANSFER:
        source_path = os.path.join(SOURCE_DIR, file)
        dest_path = os.path.join(DEST_DIR, file)
        
        if os.path.exists(source_path):
            shutil.copy2(source_path, dest_path)
            print(f"Transferred: {file}")
            transferred_count += 1
        else:
            print(f"Warning: {file} not found in the source directory")
    
    # Transfer LanceDB data if it exists
    source_lancedb = os.path.join(SOURCE_DIR, "lancedb")
    dest_lancedb = os.path.join(DEST_DIR, "lancedb")
    if os.path.exists(source_lancedb):
        shutil.copytree(source_lancedb, dest_lancedb, dirs_exist_ok=True)
        print("Transferred: LanceDB data")
        transferred_count += 1
    else:
        print("Warning: LanceDB data not found in the source directory")
    
    print(f"\nTransfer complete. {transferred_count} out of {len(FILES_TO_TRANSFER) + 1} items transferred.")

if __name__ == "__main__":
    transfer_files()