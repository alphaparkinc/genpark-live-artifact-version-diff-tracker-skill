class LiveArtifactVersionDiffTrackerClient:
    def compute_artifact_diff(self, artifact_name='pricing_table.html', original_content='<div class="price">$99</div>', revised_content='<div class="price font-bold text-green-500">$79</div>'):
        import difflib
        diff_lines = list(difflib.unified_diff(
            original_content.splitlines(), revised_content.splitlines(),
            fromfile='v1/' + artifact_name, tofile='v2/' + artifact_name, lineterm=''
        ))
        return {
            'diff_id': 'art_dif_4419',
            'artifact_name': artifact_name,
            'has_changes': bool(diff_lines),
            'added_lines_count': sum(1 for line in diff_lines if line.startswith('+') and not line.startswith('+++')),
            'removed_lines_count': sum(1 for line in diff_lines if line.startswith('-') and not line.startswith('---')),
            'unified_diff_text': '\n'.join(diff_lines),
            'checksum_sha256': 'a1b2c3d4e5f67890123456789abcdef0',
            'diff_preview_url': 'https://artifacts.canvas.genpark.ai/diffs/4419.html'
        }
