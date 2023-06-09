class Endpoints:
    # ? Job endpoints
    # * Modify a defined job with a job name, in a given workspace
    REGISTER_JOB = "/job/{workspace}/{job}"
    GET_JOB = "/job/{job}"
    GET_JOBS = "/jobs"
    DELETE_JOB = "/job/{job}"

    # ? Run endpoints
    # * Run a job that is registered with the given job name
    RUN_JOB = "/run/job/{job_id}"

    # * Modify a job run, with the runs ID
    GET_RUN_JOB = "/run/job/{run_id}"
    UPDATE_RUN_JOB = "/run/job/{run_id}"
    DELETE_RUN_JOB = "/run/job/{run_id}"

    # * Get list of all run jobs under a given registered job
    GET_JOB_RUNS = "/runs/job/{job_id}"
    # * Get amount of run jobs under a given registered job
    COUNT_JOB_RUNS = "/runs/count/{job_id}"

    # * Run a task, for a specific run/job_id
    RUN_TASK = "/run/task/{run_id}"

    # * Modify a task run via its ID
    GET_RUN_TASK = "/run/task/{task_id}"
    UPDATE_RUN_TASK = "/run/task/{task_id}"
    # * Get a list of tasks ran on a specific run/job_id
    GET_RUN_JOB_TASKS = "/runs/tasks/{run_id}"

    # ? Workspace endpoints
    # * Modify a workspace given its id
    CREATE_WORKSPACE = "/workspace/{workspace}"
    GET_WORKSPACE = "/workspace/{workspace}"
    UPDATE_WORKSPACE = "/workspace/{workspace}"
    DELETE_WORKSPACE = "/workspace/{workspace}"
