from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
import os

os.environ["GOOGLE_API_KEY"] = "your api key here"

model = GoogleGenerativeAI(
    model = "models/gemini-2.0-flash-001",
)

model2 = GoogleGenerativeAI(
    model = "models/gemini-2.0-flash-001",
)


template1 = PromptTemplate(
    template = "generate a detail report on {text}",
    input_variables = ['text']
)

template2 = PromptTemplate(
    template = "generate a 4 answer questions  on {text}",
    input_variables = ['text']
)

template3 = PromptTemplate(
    template = "Merge the report and the questions \n in -->{report} \n and --> {questions}",
    input_variables = ['report', 'questions']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'report': template1 |model |parser,
    'questions': template2 | model2 | parser,
})

merge_chain = parallel_chain | template3 | model | parser

text ={
    """What is artificial general intelligence?
Artificial general intelligence (AGI) is a theoretical field of AI research that attempts to create software with human-like intelligence and the ability to learn itself. The goal is for the software to be able to perform tasks for which it is not necessarily trained or developed. 

Current artificial intelligence (AI) technologies all operate within a predetermined set of parameters. For example, AI models trained to recognize and generate images cannot create websites. AGI is a theoretical quest to develop AI systems capable of autonomous self-control, displaying a reasonable degree of self-awareness and the ability to learn new skills. AGI can solve complex problems in situations and contexts that were not taught to it at the time of its creation. AGI with human-like capabilities remains a theoretical concept and a research goal.

What is the difference between artificial intelligence and artificial general intelligence?
Over the decades, AI researchers have identified several milestones that have significantly advanced artificial intelligence, even to degrees that mimic human intelligence in specific tasks. For example, AI synthesizers use machine learning (ML) models to extract important points from documents and generate a comprehensible summary. AI, then, is a computer science discipline that enables software to solve new and challenging tasks with human-level performance. 

In contrast, an AGI system can solve problems in various domains, like a human, without manual intervention. Instead of being limited to a specific domain, AGI can teach itself and solve problems for which it has never been trained. AGI is therefore a theoretical representation of a complete artificial intelligence that solves complex tasks with generalized human cognitive abilities. 

Some computer scientists believe that AGI is a hypothetical computer program with human-like cognitive abilities and understanding. AI systems can learn to handle unfamiliar tasks without additional training on such theories. Furthermore, the AI ​​systems we use today require extensive training before they can handle related tasks in the same domain. For example, you need to optimize a pre-trained large language model (LLM) with medical datasets before it can function consistently as a medical chatbot. 

Strong AI vs. Weak AI
Powerful AI is a fully-fledged artificial intelligence, or AGI, capable of performing tasks with human-like cognitive levels despite having little background knowledge. Science fiction often describes powerful AI as a thinking machine whose human understanding is not limited by the boundaries of the domain. 

In contrast, weak AI or narrow AI are AI systems limited to specific computer specifications, algorithms, and tasks for which they are designed. For example, previous AI models had limited memory and relied only on real-time data to make decisions. Even emerging generative AI applications with better memory retention are considered weak AI because they cannot be reused in other domains. 

What are the theoretical approaches to research on artificial general intelligence?
Achieving AGI requires a broader range of technologies, data, and interconnectivity than underpins current AI models. Creativity, perception, learning, and memory are essential to creating AI that mimics complex human behaviors. AI experts have proposed several methods to guide AGI research. 

Symbolic
The symbolic approach assumes that computer systems can develop AGI by representing human thoughts using expanding logic networks. The logic network symbolizes physical objects according to an "if else" logic, allowing the AI ​​system to interpret ideas at a higher level of thinking. However, symbolic representation cannot replicate subtle cognitive abilities at the lower level, such as perception.

Connectionist
The connectionist (or emergentist) approach focuses on replicating the structure of the human brain with a neural network architecture. Neurons in the brain can alter their transmission pathways when humans interact with external stimuli. Scientists hope that AI models adopting this subsymbolic approach will be able to reproduce human-like intelligence and demonstrate low-level cognitive abilities. Large language models are an example of AI that uses the connectionist method to understand natural languages. 
    """
}

result = merge_chain.invoke(text)

print(result)






