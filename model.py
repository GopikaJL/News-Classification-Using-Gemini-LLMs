
def create_few_shot_training_prompt(dataframe):
    """
    Creates a few-shot prompt for training/testing the Gemini model.
    
    Parameters:
    - dataframe (pd.DataFrame): Few-shot dataset containing 'category' and 'text'.
    
    Returns:
    - str: A formatted few-shot prompt.
    """
    prompt = "Classify the following articles into one of these categories: Business, Entertainment, Politics, Sport, Tech.\n\n"

    for _, row in dataframe.iterrows():
        prompt += f"Category: {row['category']}\nArticle: {row['text'][:300]}...\n\n"  # Truncate long text for brevity
    prompt += "Now classify this article:\nArticle: [INSERT TEST ARTICLE HERE]...\n\nCategory:"
    return prompt
few_shot_training_prompt = create_few_shot_training_prompt(few_shot_df)
test_article = "The Prime Minister announced a new policy to boost the economy by reducing corporate taxes."
final_training_prompt = few_shot_training_prompt.replace("[INSERT TEST ARTICLE HERE]", test_article)
response = model.generate_content(final_training_prompt)
print("Training Prompt:")
print(final_training_prompt)
print("\nModel Response:")
print(response.text)  # Adjust based on the response structure
Training Prompt:
Classify the following articles into one of these categories: Business, Entertainment, Politics, Sport, Tech.

Category: politics
Article: Kennedy to make temple address

Charles Kennedy is set to address 2,000 people at a Hindu temple as part of an appeal to ethnic minority voters.

The Liberal Democrat leader will visit the Shri Swaminarayan Mandir Temple in Neasden, north west London. He will say Labour "can no longer lay exclusive ...

Category: politics
Article: UK plan to deport terror suspects

Deals are being sought to allow the UK to deport terror suspects to their home countries without risk of them being tortured or sentenced to death.

Home Secretary Charles Clarke told the Times he hoped agreement with several countries could be reached. The move fo...

Category: politics
Article: Lib Dems' 'bold' election policy

Charles Kennedy has told voters his Liberal Democrats will offer them an "honest choice" at the next general election.

With the other two big parties battling over which will impose the lowest taxes, Mr Kennedy is going into the looming election pledged to increase...

Category: politics
Article: Choose hope over fear - Kennedy

Voters will have a clear choice between the politics of fear and the politics of hope in the next general election, said Charles Kennedy.

In his New Year message the Liberal Democrat leader said Labour and the Conservatives were united in relying on fear and "populi...

Category: politics
Article: Butler launches attack on Blair

Former civil service chief Lord Butler has criticised the way Tony Blair's government operates, accusing it of being obsessed with headlines.

He also attacked the way the Iraq war was "sold" to the public, with important warnings on the strength of the intelligence ...

Category: sport
Article: Sella wants Michalak recall

Former France centre Philippe Sella believes coach Bernard Laporte must recall Frederic Michalak to give his side any chance of beating Ireland.

Sella admitted he had been impressed by current fly-half Yann Delaigue in the RBS Six Nations to date. But he told BBC Sport:...

Category: sport
Article: O'Driscoll saves Irish blushes

Two moments of magic from Brian O'Driscoll guided Ireland to a workmanlike victory against Italy.

A pair of classic outside breaks from the Ireland captain set up tries for Geordan Murphy and Peter Stringer. Italy led 9-8 early in the second half but Stringer's try g...

Category: sport
Article: Fit-again Betsen in France squad

France have brought flanker Serge Betsen back into their squad to face England at Twickenham on Sunday.

But the player, who missed the victory over Scotland through injury, must attend a disciplinary hearing on Wednesday after being cited by Wasps. "Serge has a goo...

Category: sport
Article: Newry to fight cup exit in courts

Newry City are expected to discuss legal avenues on Friday regarding overturning their ejection from the Nationwide Irish Cup.

The IFA upheld its original decision to throw Newry out of the cup following the Andy Crawford registration row. ''A law firm will put a ...

Category: sport
Article: Sprinter Walker quits athletics

Former European 200m champion Dougie Walker is to retire from athletics after a series of six operations left him struggling for fitness.

Walker had hoped to compete in the New Year Sprint which is staged at Musselburgh Racecourse near Edinburgh on Tuesday and Wedne...

Category: tech
Article: Court mulls file-sharing future

Judges at the US Supreme Court have been hearing evidence for and against file-sharing networks.

The court will decide whether producers of file-sharing software can ultimately be held responsible for copyright infringement. They questioned if opening the way for th...

Category: tech
Article: Camera phones are 'must-haves'

Four times more mobiles with cameras in them will be sold in Europe by the end of 2004 than last year, says a report from analysts Gartner.

Globally, the number sold will reach 159 million, an increase of 104%. The report predicts that nearly 70% of all mobile phones...

Category: tech
Article: Seamen sail into biometric future

The luxury cruise liner Crystal Harmony, currently in the Gulf of Mexico, is the unlikely setting for tests of biometric technology.

As holidaymakers enjoy balmy breezes, their ship's crew is testing prototype versions of the world's first internationally issued b...

Category: tech
Article: Sony PSP tipped as a 'must-have'

Sony's Playstation Portable is the top UK gadget for 2005, according to a round-up of ultimate gizmos compiled by Stuff Magazine.

It beats the iPod into second place in the Top Ten Essentials list which predicts what gadget-lovers are likely to covet this year. Own...

Category: tech
Article: Speech takes on search engines

A Scottish firm is looking to attract web surfers with a search engine that reads out results.

Called Speegle, it has the look and feel of a normal search engine, with the added feature of being able to read out the results. Scottish speech technology firm CEC System...

Category: entertainment
Article: Foxx and Swank win US awards

Jamie Foxx and Hilary Swank have won the Screen Actors Guild Awards for best male and female film actors, boosting their Oscars hopes this month.

Foxx's portrayal of late soul-singer Ray Charles in Ray had already earned him a prestigious Golden Globe award. Swank triu...

Category: entertainment
Article: U2 stars enter rock Hall of Fame

Singer Bruce Springsteen has inducted Irish rock band U2 into the Rock and Roll Hall of Fame, in New York.

The lavish ceremony, celebrating the 50th anniversary of rock 'n' roll, also saw the induction of the Pretenders, Percy Sledge, the O'Jays and Buddy Guy. "Thi...

Category: entertainment
Article: 'My memories of Marley...'

To mark the 60th anniversary of the birth of reggae star Bob Marley, Rob Partridge - Marley's former head of press at Island Records - remembers the man behind the legend.

Partridge worked with Marley from 1977 until the Jamaican musician's death in 1981.

: "I joined Is...

Category: entertainment
Article: Berlin cheers for anti-Nazi film

A German movie about an anti-Nazi resistance heroine has drawn loud applause at Berlin Film Festival.

Sophie Scholl - The Final Days portrays the final days of the member of the White Rose movement. Scholl, 21, was arrested and beheaded with her brother, Hans, in 1...

Category: entertainment
Article: Help for indies in download sales

A campaign has been launched to help independent labels get their music online and benefit from the growing trend for downloading music.

The British Phonographic Industry has identified a lack of independent music available for download. "We want to ensure that in...

Category: business
Article: Khodorkovsky quits Yukos shares

Jailed tycoon Mikhail Khodorkovsky has transferred his controlling stake in oil giant Yukos to a business partner.

Mr Khodorkovsky handed over his entire 59.5% stake in holding company Group Menatep - which controls Yukos - to Leonid Nevzlin. A close ally of the ex-...

Category: business
Article: EU-US seeking deal on air dispute

The EU and US have agreed to begin talks on ending subsidies given to aircraft makers, EU Trade Commissioner Peter Mandelson has announced.

Both sides hope to reach a negotiated deal over state aid received by European aircraft maker Airbus and its US rival Boeing...

Category: business
Article: US economy still growing says Fed

Most areas of the US saw their economy continue to expand in December and early January, the US Federal Reserve said in its latest Beige Book report.

Of the 12 US regions it identifies for the study, 11 showed stronger economic growth, with only the Cleveland area...

Category: business
Article: BT offers equal access to rivals

BT has moved to pre-empt a possible break-up of its business by offering to cut wholesale broadband prices and open its network to rivals.

The move comes after telecom regulator Ofcom said in November that the firm must offer competitors "real equality of access to...

Category: business
Article: US trade gap ballooned in October

The US trade deficit widened by more than expected in October, hitting record levels after higher oil prices raised import costs, figures have shown

The trade shortfall was $55.5bn (£29bn), up 9% from September, the Commerce Department said. That pushed the 10 mon...

Now classify this article:
Article: The Prime Minister announced a new policy to boost the economy by reducing corporate taxes....

Category:

Model Response:
Category: Politics
# Step 1: Mark the few-shot dataset
few_shot_ids = few_shot_df.index.tolist()  # Get the indices of few-shot examples

# Step 2: Exclude few-shot examples from the original dataset
zero_shot_df = df.drop(index=few_shot_ids).reset_index(drop=True)  # Exclude few-shot rows
# Step 3: Perform Zero-Shot Testing
from sklearn.metrics import classification_report, accuracy_score


# Sample 60 articles for zero-shot testing
zero_shot_sample = zero_shot_df.sample(150, random_state=42)
print(zero_shot_sample)
true_labels = []
predicted_labels = []

# Process the articles in smaller batches
batch_size = 10  # Process 10 articles at a time
num_batches = (len(zero_shot_sample) + batch_size - 1) // batch_size  # Total batches

for batch_index in range(num_batches):
    batch_data = zero_shot_sample.iloc[batch_index * batch_size : (batch_index + 1) * batch_size]

    # Create a batch prompt
    batch_prompt = "Classify the following articles into one of these categories: Business, Entertainment, Politics, Sport, Tech.\n\n"
    
    for _, row in batch_data.iterrows():
        true_labels.append(row['category'])  # Append true category
        batch_prompt += f"Article: {row['text'][:150]}...\n\n"  # Truncate article

    batch_prompt += "Provide only the category name for each article."

    # Send a single API request for the batch
    response = model.generate_content(batch_prompt)

    # Debug: Print raw response
    print("Raw Model Response:")
    print(response.text)

    # Directly split the response into predicted labels
    batch_predictions = response.text.splitlines()  # Each line corresponds to a prediction
    predicted_labels.extend(batch_predictions)

# Ensure consistent lengths of true and predicted labels
if len(predicted_labels) < len(true_labels):
    predicted_labels.extend(["Unknown"] * (len(true_labels) - len(predicted_labels)))
elif len(predicted_labels) > len(true_labels):
    predicted_labels = predicted_labels[:len(true_labels)]
true_labels = [label.title() for label in true_labels]  # Convert to title-case
predicted_labels = [label.title() for label in predicted_labels]  # Convert to title-case

# Compute classification report and accuracy
valid_categories = ["Business", "Entertainment", "Politics", "Sport", "Tech"]

print("True Labels:", true_labels)
print("Predicted Labels:", predicted_labels)
print("Unique True Labels:", set(true_labels))
print("Unique Predicted Labels:", set(predicted_labels))

print("Classification Report:")
print(classification_report(true_labels, predicted_labels, target_names=valid_categories))

accuracy = accuracy_score(true_labels, predicted_labels)
print(f"Accuracy: {accuracy * 100:.2f}%")
category                                               text
1451  entertainment  Public show for Reynolds portrait\n\nSir Joshu...
1334  entertainment  Celebrities get to stay in jungle\n\nAll four ...
1761       business  Wembley firm won't make a profit\n\nShares in ...
1735       business  Shares rise on new Man Utd offer\n\nShares in ...
1576  entertainment  Jarre joins fairytale celebration\n\nFrench mu...
...             ...                                                ...
135        politics  Security papers 'found in street'\n\nAn inquir...
1501  entertainment  Connick Jr to lead Broadway show\n\nSinger and...
1855       business  Metlife buys up Citigroup insurer\n\nUS bankin...
360        politics  Lord Scarman, 93, dies peacefully\n\nDistingui...
538           sport  Wright-Phillips to start on right\n\nEngland c...

[150 rows x 2 columns]
Raw Model Response:
Entertainment
Entertainment
Business
Business
Entertainment
Tech
Entertainment
Sport
Sport
Sport

Raw Model Response:
Sport
Business
Tech
Business
Business
Tech
Entertainment
Politics
Business
Entertainment

Raw Model Response:
Business
Business
Entertainment
Business
Politics
Business
Sport
Entertainment
Sport
Politics

Raw Model Response:
Sport
Sport
Business
Sport
Business
Sport
Business
Politics
Politics
Politics

Raw Model Response:
Business
Tech
Sport
Politics
Sport
Politics
Sport
Politics
Entertainment
Politics

Raw Model Response:
Sport
Business
Tech
Sport
Business
Politics
Business
Entertainment
Tech
Sport

Raw Model Response:
Entertainment
Business
Sport
Entertainment
Business
Sport
Politics
Politics
Entertainment
Sport

Raw Model Response:
Entertainment
Politics
Business
Tech
Sport
Sport
Tech
Business
Entertainment
Entertainment

Raw Model Response:
Business
Politics
Politics
Sport
Entertainment
Tech
Business
Sport
Sport
Tech

Raw Model Response:
Politics
Sport
Business
Business
Sport
Sport
Politics
Tech
Sport
Sport

Raw Model Response:
Business
Politics
Business
Entertainment
Entertainment
Politics
Entertainment
Tech
Sport
Sport

Raw Model Response:
Sport
Business
Business
Tech
Sport
Politics
Politics
Business
Tech
Politics

Raw Model Response:
Sport
Tech
Sport
Business
Politics
Sport
Business
Politics
Tech
Sport

Raw Model Response:
Tech
Politics
Entertainment
Politics
Business
Entertainment
Sport
Tech
Tech
Entertainment

Raw Model Response:
Politics
Entertainment
Sport
Sport
Politics
Politics
Entertainment
Business
Politics
Sport

True Labels: ['Entertainment', 'Entertainment', 'Business', 'Business', 'Entertainment', 'Tech', 'Entertainment', 'Sport', 'Sport', 'Sport', 'Sport', 'Business', 'Tech', 'Business', 'Business', 'Tech', 'Entertainment', 'Politics', 'Business', 'Entertainment', 'Business', 'Business', 'Entertainment', 'Business', 'Politics', 'Business', 'Sport', 'Entertainment', 'Sport', 'Politics', 'Sport', 'Sport', 'Business', 'Sport', 'Business', 'Sport', 'Business', 'Politics', 'Politics', 'Politics', 'Business', 'Tech', 'Sport', 'Politics', 'Sport', 'Politics', 'Sport', 'Business', 'Entertainment', 'Politics', 'Sport', 'Business', 'Tech', 'Sport', 'Business', 'Politics', 'Business', 'Entertainment', 'Tech', 'Sport', 'Entertainment', 'Business', 'Sport', 'Entertainment', 'Business', 'Sport', 'Business', 'Politics', 'Entertainment', 'Sport', 'Entertainment', 'Business', 'Business', 'Tech', 'Sport', 'Business', 'Tech', 'Business', 'Entertainment', 'Entertainment', 'Business', 'Politics', 'Politics', 'Sport', 'Entertainment', 'Tech', 'Business', 'Sport', 'Sport', 'Tech', 'Politics', 'Sport', 'Business', 'Business', 'Sport', 'Sport', 'Politics', 'Business', 'Sport', 'Sport', 'Business', 'Politics', 'Business', 'Entertainment', 'Entertainment', 'Politics', 'Entertainment', 'Tech', 'Sport', 'Sport', 'Tech', 'Business', 'Business', 'Tech', 'Sport', 'Politics', 'Politics', 'Business', 'Tech', 'Politics', 'Sport', 'Tech', 'Sport', 'Business', 'Politics', 'Sport', 'Business', 'Politics', 'Tech', 'Sport', 'Tech', 'Politics', 'Tech', 'Politics', 'Business', 'Entertainment', 'Sport', 'Tech', 'Tech', 'Entertainment', 'Politics', 'Entertainment', 'Sport', 'Sport', 'Business', 'Politics', 'Entertainment', 'Business', 'Politics', 'Sport']
Predicted Labels: ['Entertainment', 'Entertainment', 'Business', 'Business', 'Entertainment', 'Tech', 'Entertainment', 'Sport', 'Sport', 'Sport', 'Sport', 'Business', 'Tech', 'Business', 'Business', 'Tech', 'Entertainment', 'Politics', 'Business', 'Entertainment', 'Business', 'Business', 'Entertainment', 'Business', 'Politics', 'Business', 'Sport', 'Entertainment', 'Sport', 'Politics', 'Sport', 'Sport', 'Business', 'Sport', 'Business', 'Sport', 'Business', 'Politics', 'Politics', 'Politics', 'Business', 'Tech', 'Sport', 'Politics', 'Sport', 'Politics', 'Sport', 'Politics', 'Entertainment', 'Politics', 'Sport', 'Business', 'Tech', 'Sport', 'Business', 'Politics', 'Business', 'Entertainment', 'Tech', 'Sport', 'Entertainment', 'Business', 'Sport', 'Entertainment', 'Business', 'Sport', 'Politics', 'Politics', 'Entertainment', 'Sport', 'Entertainment', 'Politics', 'Business', 'Tech', 'Sport', 'Sport', 'Tech', 'Business', 'Entertainment', 'Entertainment', 'Business', 'Politics', 'Politics', 'Sport', 'Entertainment', 'Tech', 'Business', 'Sport', 'Sport', 'Tech', 'Politics', 'Sport', 'Business', 'Business', 'Sport', 'Sport', 'Politics', 'Tech', 'Sport', 'Sport', 'Business', 'Politics', 'Business', 'Entertainment', 'Entertainment', 'Politics', 'Entertainment', 'Tech', 'Sport', 'Sport', 'Sport', 'Business', 'Business', 'Tech', 'Sport', 'Politics', 'Politics', 'Business', 'Tech', 'Politics', 'Sport', 'Tech', 'Sport', 'Business', 'Politics', 'Sport', 'Business', 'Politics', 'Tech', 'Sport', 'Tech', 'Politics', 'Entertainment', 'Politics', 'Business', 'Entertainment', 'Sport', 'Tech', 'Tech', 'Entertainment', 'Politics', 'Entertainment', 'Sport', 'Sport', 'Politics', 'Politics', 'Entertainment', 'Business', 'Politics', 'Sport']
Unique True Labels: {'Entertainment', 'Tech', 'Sport', 'Business', 'Politics'}
Unique Predicted Labels: {'Entertainment', 'Tech', 'Sport', 'Business', 'Politics'}
Classification Report:
               precision    recall  f1-score   support

     Business       1.00      0.85      0.92        40
Entertainment       0.96      1.00      0.98        24
     Politics       0.87      1.00      0.93        27
        Sport       0.95      1.00      0.97        39
         Tech       0.95      0.90      0.92        20

     accuracy                           0.95       150
    macro avg       0.95      0.95      0.95       150
 weighted avg       0.95      0.95      0.95       150

Accuracy: 94.67%
