python actor_critic.py --baseline --discount=0.99 --epsilon=0.01 --lr_critic=0.5 --lr_intra=0.25 --lr_term=0.25 --nruns=350 --nsteps=1000 --nepisodes=2000 --env_id="SubGoalFourrooms-v0" --subgoal-path="human_subgoals/eval_20190508.csv"
# python actor_critic.py --baseline --discount=0.99 --epsilon=0.01 --lr_critic=0.5 --lr_intra=0.25 --lr_term=0.25 --nruns=350 --nsteps=1000 --nepisodes=2000 --env_id="Fourrooms-v0"
# python actor_critic.py --baseline --discount=0.99 --epsilon=0.01 --lr_critic=0.5 --lr_intra=0.25 --lr_term=0.25 --nruns=350 --nsteps=1000 --nepisodes=2000 --env_id="ShapingFourrooms-v0"