def split_earnings(dataframe: pd.DataFrame=None):

    output = []

    for r in dataframe.to_dict('records'):
        # id -er
        tagged = r['tagged']
        if tagged == 'NoScript':
            output.append({
                'presentation':'NoScript',
                'qa_session':'NoScript'})

        else:
            #print(row['transcript'])
            script = [line.lower().replace('\n', '') for line in r['transcript'] ]
            
            # This pattern will match all the mentioned variations
            patterns = ['question-and-answer session', \
                'questions-and-answers session', \
                'question and answer session', \
                'questions and answers session', \
                'question-and-answer session ']
            
            qa_index = None
            for inde, line in enumerate(script):
                if line in patterns:
                    qa_index = inde
                    break

            if qa_index is not None:
            
                presentation = script[:qa_index]
                qa_session = script[qa_index:]

                output.append({
                    'presentation':presentation,
                    'qa_session':qa_session})
            
            else:
                presentation = script
                qa_session = 'no_qa_session'
                output.append({
                    'presentation':presentation,
                    'qa_session': qa_session})
    
    dataframe = pd.concat([dataframe, pd.DataFrame(output)], axis=1)
    return dataframe
