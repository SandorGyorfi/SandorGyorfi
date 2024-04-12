from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0011_poll_polloption_vote_delete_comment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="polloption",
            name="poll",
        ),
        migrations.AlterUniqueTogether(
            name="vote",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="vote",
            name="user",
        ),
        migrations.AddField(
            model_name="blogpost",
            name="game_changer_votes",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="blogpost",
            name="interesting_votes",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="blogpost",
            name="meh_votes",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="blogpost",
            name="needs_work_votes",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name="Poll",
        ),
    ]