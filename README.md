# Source Sentry example

A small repository that shows [Source Sentry](https://git.gabmacn.com/gmn/source-sentry)
at work, and tests its GitHub Actions recipe on real CI.

The "service" is two settings files, and two documents describe them:

| Document | Describes | Class |
|---|---|---|
| [`docs/guide.md`](docs/guide.md) | [`src/settings.py`](src/settings.py): the port and the rate limit | none |
| [`docs/privacy.md`](docs/privacy.md) | [`src/storage.py`](src/storage.py): what is kept, and for how long | `privacy` |

Each document's frontmatter records its sources and the versions of them
that were last reviewed. [`.source-sentry/source-sentry.yaml`](.source-sentry/source-sentry.yaml)
defines two contexts:

- **`default`**, for pull requests and pushes: a document whose sources
  changed is due at once, and warns.
- **`production`**, for deploys: a privacy policy that no longer matches the
  code fails, so the deploy waits for it.

[`.github/workflows/source-sentry.yml`](.github/workflows/source-sentry.yml)
is Source Sentry's GitHub Actions recipe, pinned to a release by version and
checksum. On every pull request and push it runs the report gate
(`check --fail-on warn`, not required) and the continue gate
(`check --fail-on fail`, required). On a push to `main` it also runs the
production gate, which the placeholder deploy job waits for.

## Trying it

Change `PORT` in `src/settings.py`, then:

```sh
source-sentry check                   # docs/guide.md is now due
source-sentry diff docs/guide.md      # what changed since its review
# Update docs/guide.md to match, then record the review:
source-sentry attest docs/guide.md
```

A pull request with the same change shows the report gate failing while
the continue gate passes. A change to `src/storage.py` pushed to `main`
without updating the privacy policy fails the production gate, and the
deploy does not run.
