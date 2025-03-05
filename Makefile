.PHONY: test format clean

test:
		pytest tests/	

format:
		black src/ tests/
		isort src/ tests/


clean:
		rm -rf logs/*.log reports/*.csv
