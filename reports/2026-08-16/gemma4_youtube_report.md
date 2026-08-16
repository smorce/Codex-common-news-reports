# YouTube Video Summary Report (Error)

- Generated at: 2026-08-16T00:11:06Z
- Status: Failed

## Error

gemma4_e2b_video_summary.py exited with code 1.

## Details

```
Press Room 119'
       https://www.youtube.com/watch?v=-mNgZHTLpmw
[INFO] Candidate #14: '靴×ショーツ×トップスの失敗しない合わせ術！ジャンル別の正解を導き出せ！| B.R. Fashion College Lesson.893 ショートパンツ特集'
       https://www.youtube.com/watch?v=-a1vhlAfx3k
[INFO] Candidate #15: '女子も憧れるイケオジな着こなし提案！Z世代男子に着て欲しい大人の渋コーデ♪'
       https://www.youtube.com/watch?v=Evobrnz3yJM
Traceback (most recent call last):
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1745, in <module>
    main()
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 1667, in main
    model, processor = load_gemma_model(args.model)
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\kbpsh\OneDrive\development\project\Codex_common_news_reports\gemma4_e2b_video_summary.py", line 978, in load_gemma_model
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
