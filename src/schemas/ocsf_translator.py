# Copyright 2025 Kyle Walkley
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from schemas.base_schema_translator import BaseSchemaTranslator
from inference.base_translator_agent import BaseTranslatorAgent
import utils
import schemas.definitions.ocsf_definition as ocsf

class OCSFTranslator(BaseSchemaTranslator):

    def infer_category(self, sample:str) -> str:
        '''Returns the inferred OCSF category name for the provided sample'''
        
        prompt = f'''Choose the OCSF category the following input best aligns with given the following context. Respond with just the proper category name.

                Context: {utils.get_text_from_url(ocsf.OCSF_BASE, 'html.parser')}

                Input: {sample}'''
        
        return self.agent.generate(prompt)

    def infer_class(self, sample:str, ocsf_category:str):
        '''Returns the inferred OCSF class name for the provided sample. The function assumes the proivided category is correct.'''

        prompt = f'''Provided the following sample and OCSF category, what OCSF class type best aligns with the input? Respond with only the class type name.

                Context: Category - {ocsf_category}

                Activity Type Context: {utils.get_text_from_url(ocsf.OCSF_CATEGORIES[ocsf_category], 'html.parser')}

                Input: {sample}'''
        
        return self.agent.generate(prompt)
    
    def infer_ocsf_schema(self, ocsf_category:str, ocsf_class:str):
        '''Returns all fields and subfields in a json string mapped to whether a field is required or not'''

        prompt = f'''List me all of the fields in the name column from the following schema definition. 
                 Show only the fields that do not have an extension profile tag.

                 Context: {utils.get_text_from_url(ocsf.OCSF_CLASSES[ocsf_category][ocsf_class], 'html.parser')}

                
        '''

        return self.agent.generate(prompt)
    
    def infer_mapping(self, sample:str, ocsf_category:str, ocsf_class:str):
        '''Returns the inferred translation field mappings from the sample to OCSF fields assuming the OCSF category and class'''

        prompt = f'''Translate the field names in the provided sample to OCSF. 
                  The sample aligns with the {ocsf_category} OCSF category and the {ocsf_class} OCSF class.

                  Use this as the proper OCSF schema: {utils.get_text_from_url(ocsf.OCSF_CLASSES[ocsf_category][ocsf_class], 'html5lib')}
                  Only use the fields that are labelled as required unless provided in the sample. Do not list fields labelled optional or recommended.

                  Here is the sample to translate: {sample}

                  The output should be a json object where the keys are the original sample field names and the values are the OCSF translated field names.
        '''

        return self.agent.generate(prompt)

    def get_example_record(self, ocsf_category:str, ocsf_class:str):
        '''Returns a example record based on the provided ocsf category and class'''

        prompt = f'''Provide a sample JSON record in OCSF format for the {ocsf_category} category and {ocsf_class} class type.
                  Ensure that the sample record strictly adheres to the OCSF format. Do not include any extension fields or any optional fields that would not normally be included.'''

        return self.agent.generate(prompt)

    def get_required_fields(self, ocsf_category:str, ocsf_class:str):
        '''Returns a list of all required fields for the provied OCSF category and class'''

        prompt = f'''List all of the fields listed as required in the following OCSF specification for {ocsf_category} category and {ocsf_class} class.

                  Use this as the proper OCSF schema: {utils.get_text_from_url(ocsf.OCSF_CLASSES[ocsf_category][ocsf_class], 'html5lib')}

                  The output should be ONLY a comma separate list of the required fields and nothing else.'''

        return self.agent.generate(prompt)

    def translate(self, sample:str):
        ocsf_category = self.infer_category(sample)
        print(f'The inferred OCSF category is: {ocsf_category}')

        ocsf_class = self.infer_class(sample, ocsf_category)
        print(f'The inferred OCSF class is: {ocsf_class}')

        mapping = self.infer_mapping(sample, ocsf_category, ocsf_class)
        print('\nInferred Mapping:')
        print('\n-------------------------------\n')
        print(mapping)

        print('\n')
        print('Required fields: ', self.get_required_fields(ocsf_category, ocsf_class))


    @classmethod
    def name(cls):
        return 'OCSF'
    
    def __init__(self, agent:BaseTranslatorAgent):
        super().__init__()
        self.agent = agent