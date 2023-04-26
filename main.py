from database.surreal import SurrealDatabase

if __name__ == "__main__":
    surreal = SurrealDatabase()

    print(
        surreal.register_job(
            workspace_id="temp_workspace", job_name="my cool job 2", tags=["epic tag"]
        )
    )

    print(surreal.get_jobs())
