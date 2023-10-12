from narrative_generator import generate_narrative

def main() -> None:
    generated_narrative = generate_narrative()
    
    with open('output.txt', 'w') as f:
        f.write(generated_narrative)
    
if __name__ == "__main__":
    main() 
    