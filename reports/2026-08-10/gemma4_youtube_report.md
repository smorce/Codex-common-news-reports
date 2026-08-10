# YouTube Video Summary Report (Error)

- Generated at: 2026-08-10T00:06:39Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
, follow_redirects=follow_redirects)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\.venv\Lib\site-packages\httpx\_client.py", line 901, in send
    raise RuntimeError("Cannot send a request, as the client has been closed.")
RuntimeError: Cannot send a request, as the client has been closed.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1745, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1667, in main
    model, processor = load_gemma_model(args.model)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 983, in load_gemma_model
    processor = AutoProcessor.from_pretrained(model_name)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\.venv\Lib\site-packages\transformers\models\auto\processing_auto.py", line 328, in from_pretrained
    config_dict, _ = ProcessorMixin.get_processor_dict(pretrained_model_name_or_path, **kwargs)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\.venv\Lib\site-packages\transformers\processing_utils.py", line 1063, in get_processor_dict
    raise OSError(
OSError: Can't load processor for 'google/gemma-4-E2B-it'. If you were trying to load it from 'https://huggingface.co/models', make sure you don't have a local directory with the same name. Otherwise, make sure 'google/gemma-4-E2B-it' is the correct path to a directory containing a processor_config.json file

```
