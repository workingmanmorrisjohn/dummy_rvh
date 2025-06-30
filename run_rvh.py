from pathlib import Path
import shutil

from src.config import REGISTERED_OBJ_DIR

async def ipnet_register_mesh(avatar_id: str, obj_filepath: Path, avatar_gender: str) -> Path:
    output_path = REGISTERED_OBJ_DIR / f"{avatar_id}_{avatar_gender}_registered.pkl"
    
    shutil.copy(obj_filepath, output_path)
    
    return output_path