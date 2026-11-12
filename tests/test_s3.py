from click.testing import CliRunner
from moto import mock_aws
from cloudops.main import cli


@mock_aws
def test_s3_create_and_list_bucket():
    runner = CliRunner()

    create_res = runner.invoke(cli, ["s3-create", "ziad-cloudops-test-bucket"])
    assert create_res.exit_code == 0
    assert "Created bucket: ziad-cloudops-test-bucket" in create_res.output

    list_res = runner.invoke(cli, ["s3-list"])
    assert list_res.exit_code == 0
    assert "ziad-cloudops-test-bucket" in list_res.output