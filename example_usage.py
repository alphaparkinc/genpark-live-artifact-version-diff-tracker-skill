from client import LiveArtifactVersionDiffTrackerClient

def main():
    client = LiveArtifactVersionDiffTrackerClient()
    res = client.compute_artifact_diff()
    print('Live Artifact Diff Tracker: ' + res['diff_id'] + ' (' + res['artifact_name'] + ')')
    print('Lines Added: +' + str(res['added_lines_count']) + ' | Removed: -' + str(res['removed_lines_count']))
    print('Unified Diff:\n' + res['unified_diff_text'])
    print('Preview URL: ' + res['diff_preview_url'])

if __name__ == '__main__':
    main()
