# YouTube Video Summary Report (Error)

- Generated at: 2026-05-06T00:19:29Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
ww.youtube.com/watch?v=KwNACUYwU48
[INFO] RSS #2: 'ビヨンセ、レディー・ガガ…数々の著名人を撮るレスリー・キーの成功の鍵とは？｜B.R.CHANNEL THE INTUITION #14'
       https://www.youtube.com/watch?v=mgF8yPNJUvk
[INFO] RSS #3: 'コスパも優秀！今人気の2大ブランド複合店が爆誕！6月のおでかけコーデ提案 | B.R. Fashion College Lesson.876 ブリリア1949＆フィリッポ デ ローレンティス'
       https://www.youtube.com/watch?v=5wj7hYNetC0
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1549, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1499, in main
    model, processor = load_gemma_model(args.model)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 830, in load_gemma_model
    model = AutoModelForMultimodalLM.from_pretrained(
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\.venv\Lib\site-packages\transformers\models\auto\auto_factory.py", line 387, in from_pretrained
    return model_class.from_pretrained(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\.venv\Lib\site-packages\transformers\modeling_utils.py", line 4135, in from_pretrained
    loading_info, disk_offload_index = cls._load_pretrained_model(model, state_dict, checkpoint_files, load_config)
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\.venv\Lib\site-packages\transformers\modeling_utils.py", line 4243, in _load_pretrained_model
    file_pointer = safe_open(file, framework="pt", device="cpu")
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: ページング ファイルが小さすぎるため、この操作を完了できません。 (os error 1455)

```
