import os
import json
from bs4 import BeautifulSoup
import re

def extract_text_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
        return ' '.join(soup.stripped_strings)

def extract_metadata(filename):
    ors_match = re.search(r'ors_(\d+[A-Za-z]?\.\d+)', filename)
    chapter_match = re.search(r'chapter_(\d+[A-Za-z]?)', filename)
    title_match = re.search(r'title_(\d+[A-Za-z]?)', filename)
    volume_match = re.search(r'volume_(\d+)', filename)

    return {
        'ors': ors_match.group(1) if ors_match else 'N/A',
        'chapter': chapter_match.group(1) if chapter_match else 'N/A',
        'title': title_match.group(1) if title_match else 'N/A',
        'volume': volume_match.group(1) if volume_match else 'N/A'
    }

def extract_metadata_from_content(content):
    chapter_match = re.search(r'Chapter (\d+[A-Za-z]?)', content)
    title_match = re.search(r'Title (\d+)', content)
    volume_match = re.search(r'Volume (\d+)', content)

    return {
        'chapter': chapter_match.group(1) if chapter_match else 'N/A',
        'title': title_match.group(1) if title_match else 'N/A',
        'volume': volume_match.group(1) if volume_match else 'N/A'
    }

def main():
    base_url = 'https://oregon.public.law/'
    directory = './statutes'  # Statutes directory
    output_file = 'output.jsonl'
    page_id = 1

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in os.listdir(directory):
            if filename.startswith('ors_'):
                file_path = os.path.join(directory, filename)
                relative_path = os.path.relpath(file_path, '.')
                url = base_url + relative_path.replace('\\', '/')
                
                content = extract_text_from_html(file_path)
                filename_metadata = extract_metadata(filename)
                content_metadata = extract_metadata_from_content(content)
                
                data = {
                    'url': url,
                    'page_id': page_id,
                    'content': content,
                    'ors': filename_metadata['ors'],
                    'chapter': filename_metadata['chapter'] if filename_metadata['chapter'] != 'N/A' else content_metadata['chapter'],
                    'title': filename_metadata['title'] if filename_metadata['title'] != 'N/A' else content_metadata['title'],
                    'volume': filename_metadata['volume'] if filename_metadata['volume'] != 'N/A' else content_metadata['volume']
                }
                
                json.dump(data, outfile, ensure_ascii=False)
                outfile.write('\n')
                
                page_id += 1
                print(f"Processed: {filename}")

    print(f"Extraction complete. Output saved to {output_file}")

if __name__ == "__main__":
    main()
