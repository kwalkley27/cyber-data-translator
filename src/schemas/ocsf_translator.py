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

                Context: {utils.get_text_from_url(ocsf.OCSF_BASE)}

                Input: {sample}'''
        
        return self.agent.generate(prompt)

    def infer_class(self, sample:str, ocsf_category:str):
        '''Returns the inferred OCSF class name for the provided sample. The function assumes the proivided category is correct.'''

        prompt = f'''Provided the following sample and OCSF category, what OCSF class type best aligns with the input? Respond with only the class type name.

                Context: Category - {ocsf_category}

                Activity Type Context: {utils.get_text_from_url(ocsf.OCSF_CATEGORIES[ocsf_category])}

                Input: {sample}'''
        
        return self.agent.generate(prompt)
    
    def infer_ocsf_schema(self, ocsf_category:str, ocsf_class:str):
        '''Returns all fields and subfields in a json string mapped to whether a field is required or not'''

        prompt = f'''Provided the following OCSF definition for the {ocsf_category} category and the {ocsf_class} class,
                return a json string that shows all fields and subfields for this OCSF category and class mapped to a boolean value of whether the field is required.
                For example, if the definition shows field1, field2, and field3 and field1 is required but field2 and field3 are optional or recommended, you should return {{"field1":true, "field2":false, "field3":false}}

                Use only the fields outlined in the name column of the field definitions listed below.

                Field definitions: {utils.get_text_from_url(ocsf.OCSF_CLASSES[ocsf_category][ocsf_class])}

                Pretty print the output so its easy to read.
        '''

        return self.agent.generate(prompt)

    def infer_mapping(self, sample:str, ocsf_category:str, ocsf_class:str):
        '''Returns the inferred translation field mappings from the sample to OCSF fields assuming the OCSF category and class'''

        prompt = f'''Translate the field names in the provided sample to OCSF. The sample aligns with the {ocsf_category} OCSF category and the {ocsf_class} OCSF class.

        Use this as the proper OCSF field definitions: {utils.get_text_from_url(ocsf.OCSF_CLASSES[ocsf_category][ocsf_class])}

        If a field in the OCSF class maps to an object, make sure the proper object fields are defined as well. These are the definitions for all OCSF objects, use only the ones defined in the OCSF class definition: {utils.get_text_from_url(ocsf.OCSF_OBJECTS)}

        Here is the sample to translate: {sample}

        The output should be a json object where the keys are the original sample field names and the values are the OCSF translated field names. 
        Make sure that all OCSF required fields for the proper {ocsf_category} category and {ocsf_class} class are listed. 
        If no OCSF mapping for a field can be found, put it in an _unmapped field of type list.
        If there are required OCSF fields without mappings found in the sample, put these OCSF field names in a _required field of type list.
        '''

        return self.agent.generate(prompt)


    def translate(self, sample:str):
        ocsf_category = self.infer_category(sample)
        print(f'The inferred OCSF category is: {ocsf_category}')

        ocsf_class = self.infer_class(sample, ocsf_category)
        print(f'The inferred OCSF class is: {ocsf_class}')

        #mapping = self.infer_mapping(sample, ocsf_category, ocsf_class)
        #print('Inferred Mapping:')
        #print('\n-------------------------------\n')
        #print(mapping)

        ocsf_schema = self.infer_ocsf_schema(ocsf_category, ocsf_class)
        print('Inferred OCSF schema:')
        print('\n------------------------\n')
        print(ocsf_schema)

    @classmethod
    def name(cls):
        return 'OCSF'
    
    def __init__(self, agent:BaseTranslatorAgent):
        super().__init__()
        self.agent = agent