import unreal
def main():
    print("Script started.")


    unreal.EditorLoadingAndSavingUtils.load_map("/Game/map")
    print("Map loaded successfully.")

    editor_actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    

    actors = editor_actor_subsystem.get_all_level_actors()
    

    bp_actor = None
    for actor in actors:
        if actor.get_actor_label() == "MapBLD": 
            bp_actor = actor
            break

    if bp_actor is not None:
        print(f"Actor {bp_actor.get_actor_label()} found")
        

        bp_function_name = "Run"
        try:
            bp_actor.call_method("Run")
            print(f"Function {bp_function_name} runned successfully")
        except Exception as e:
            print(f"Error in {bp_function_name}: {e}")
    else:
        print("Actor not found.")
    
    level_editor_subsystem = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
    if level_editor_subsystem:
        level_editor_subsystem.save_current_level()
        print("Level saved successfully.")
    else:
        print("Failed to get Level Editor Subsystem.") 

if __name__ == "__main__":
    main()