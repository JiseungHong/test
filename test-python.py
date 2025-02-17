import argparse
import os
import logging

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Resolve issues from Github.")
    parser.add_argument(
        "--llm-models",
        type=str,
        default=None,
        help="LLM models to use.",
    )
    my_args = parser.parse_args()
    models = my_args.llm_models or os.environ["LLM_MODELS"]
    logger.info(f"Models: {models}")
    logger.info("Python file successfully executed!")

if __name__ == "__main__":
    main()