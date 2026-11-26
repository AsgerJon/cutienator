//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextdocumentfragment.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextdocumentfragment.h>
#include <QtGui/qtextcursor.h>
#include <QtCore/qstring.h>

//  QTextDocumentFragment::QTextDocumentFragment()
extern "C" Q_DECL_EXPORT
QTextDocumentFragment *ritual_ZN21QTextDocumentFragmentC1Ev() {
  return new QTextDocumentFragment();
}

//  QTextDocumentFragment::QTextDocumentFragment(const QTextDocument
//      *document)
extern "C" Q_DECL_EXPORT
QTextDocumentFragment *ritual_ZN21QTextDocumentFragmentC1EPK13QTextDocument(
    const QTextDocument *document) {
  return new QTextDocumentFragment(document);
}

//  QTextDocumentFragment::QTextDocumentFragment(const QTextCursor &range)
extern "C" Q_DECL_EXPORT
QTextDocumentFragment *ritual_ZN21QTextDocumentFragmentC1ERK11QTextCursor(
    const QTextCursor *range) {
  return new QTextDocumentFragment(*range);
}

//  QTextDocumentFragment::QTextDocumentFragment(const QTextDocumentFragment
//      &rhs)
extern "C" Q_DECL_EXPORT
QTextDocumentFragment *ritual_ZN21QTextDocumentFragmentC1ERKS_(
    const QTextDocumentFragment *rhs) {
  return new QTextDocumentFragment(*rhs);
}

//  QTextDocumentFragment &QTextDocumentFragment::operator=(const
//      QTextDocumentFragment &rhs)
extern "C" Q_DECL_EXPORT
QTextDocumentFragment *ritual_ZN21QTextDocumentFragmentaSERKS_(
    QTextDocumentFragment *self,
    const QTextDocumentFragment *rhs) {
  return &(self->operator=(*rhs));
}

//  QTextDocumentFragment::~QTextDocumentFragment()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTextDocumentFragmentD1Ev(QTextDocumentFragment *self) {
  delete self;
}

//  bool QTextDocumentFragment::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QTextDocumentFragment7isEmptyEv(
    const QTextDocumentFragment *self) {
  return self->isEmpty();
}

//  QString QTextDocumentFragment::toPlainText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QTextDocumentFragment11toPlainTextEv(
    const QTextDocumentFragment *self) {
  return new QString(self->toPlainText());
}

//  QString QTextDocumentFragment::toRawText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QTextDocumentFragment9toRawTextEv(
    const QTextDocumentFragment *self) {
  return new QString(self->toRawText());
}

#if !defined(QT_NO_TEXTHTMLPARSER)
//  QString QTextDocumentFragment::toHtml() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QTextDocumentFragment6toHtmlEv(
    const QTextDocumentFragment *self) {
  return new QString(self->toHtml());
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

#if QT_CONFIG(textmarkdownwriter)
//  QString QTextDocumentFragment::toMarkdown(QTextDocument::MarkdownFeatures
//      features) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QTextDocumentFragment10toMarkdownE6QFlagsIN13QTextDocument15MarkdownFeatureEE(
    const QTextDocumentFragment *self,
    int features) {
  return new QString(
      self->toMarkdown(
          QFlags<QTextDocument::MarkdownFeature>::fromInt(features)));
}
#endif  // QT_CONFIG(textmarkdownwriter)

//  QTextDocumentFragment QTextDocumentFragment::fromPlainText(const QString
//      &plainText)
extern "C" Q_DECL_EXPORT
QTextDocumentFragment *ritual_ZN21QTextDocumentFragment13fromPlainTextERK7QString(
    const QString *plainText) {
  return new QTextDocumentFragment(
      QTextDocumentFragment::fromPlainText(
          *plainText));
}

#if !defined(QT_NO_TEXTHTMLPARSER)
//  QTextDocumentFragment QTextDocumentFragment::fromHtml(const QString
//      &html, const QTextDocument *resourceProvider)
extern "C" Q_DECL_EXPORT
QTextDocumentFragment *ritual_ZN21QTextDocumentFragment8fromHtmlERK7QStringPK13QTextDocument(
    const QString *html,
    const QTextDocument *resourceProvider) {
  return new QTextDocumentFragment(
      QTextDocumentFragment::fromHtml(
          *html,
          resourceProvider));
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

#if QT_CONFIG(textmarkdownreader)
//  QTextDocumentFragment QTextDocumentFragment::fromMarkdown(const QString
//      &markdown, QTextDocument::MarkdownFeatures features)
extern "C" Q_DECL_EXPORT
QTextDocumentFragment *ritual_ZN21QTextDocumentFragment12fromMarkdownERK7QString6QFlagsIN13QTextDocument15MarkdownFeatureEE(
    const QString *markdown,
    int features) {
  return new QTextDocumentFragment(
      QTextDocumentFragment::fromMarkdown(
          *markdown,
          QFlags<QTextDocument::MarkdownFeature>::fromInt(features)));
}
#endif  // QT_CONFIG(textmarkdownreader)
