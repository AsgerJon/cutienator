//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextmarkdownwriter_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(textmarkdownwriter)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextmarkdownwriter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtextobject.h>
#include <QtCore/qstring.h>

//  QTextMarkdownWriter::QTextMarkdownWriter(QTextStream &stream,
//      QTextDocument::MarkdownFeatures features)
extern "C" Q_DECL_EXPORT
QTextMarkdownWriter *ritual_ZN19QTextMarkdownWriterC1ER11QTextStream6QFlagsIN13QTextDocument15MarkdownFeatureEE(
    QTextStream *stream,
    int features) {
  return new QTextMarkdownWriter(
      *stream,
      QFlags<QTextDocument::MarkdownFeature>::fromInt(features));
}

//  bool QTextMarkdownWriter::writeAll(const QTextDocument *document)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QTextMarkdownWriter8writeAllEPK13QTextDocument(
    QTextMarkdownWriter *self,
    const QTextDocument *document) {
  return self->writeAll(document);
}

#if QT_CONFIG(itemmodel)
//  void QTextMarkdownWriter::writeTable(const QAbstractItemModel *table)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextMarkdownWriter10writeTableEPK18QAbstractItemModel(
    QTextMarkdownWriter *self,
    const QAbstractItemModel *table) {
  self->writeTable(table);
}
#endif  // QT_CONFIG(itemmodel)

//  int QTextMarkdownWriter::writeBlock(const QTextBlock &block, bool table,
//      bool ignoreFormat, bool ignoreEmpty)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QTextMarkdownWriter10writeBlockERK10QTextBlockbbb(
    QTextMarkdownWriter *self,
    const QTextBlock *block,
    bool table,
    bool ignoreFormat,
    bool ignoreEmpty) {
  return self->writeBlock(*block, table, ignoreFormat, ignoreEmpty);
}

//  void QTextMarkdownWriter::writeFrame(const QTextFrame *frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextMarkdownWriter10writeFrameEPK10QTextFrame(
    QTextMarkdownWriter *self,
    const QTextFrame *frame) {
  self->writeFrame(frame);
}

//  void QTextMarkdownWriter::writeFrontMatter(const QString &fm)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextMarkdownWriter16writeFrontMatterERK7QString(
    QTextMarkdownWriter *self,
    const QString *fm) {
  self->writeFrontMatter(*fm);
}

//  ListInfo QTextMarkdownWriter::listInfo(QTextList *list)
extern "C" Q_DECL_EXPORT
QTextMarkdownWriter::ListInfo *ritual_ZN19QTextMarkdownWriter8listInfoEP9QTextList(
    QTextMarkdownWriter *self,
    QTextList *list) {
  return new QTextMarkdownWriter::ListInfo(self->listInfo(list));
}

//  void QTextMarkdownWriter::setLinePrefixForBlockQuote(int level)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextMarkdownWriter26setLinePrefixForBlockQuoteEi(
    QTextMarkdownWriter *self,
    int level) {
  self->setLinePrefixForBlockQuote(level);
}

//  QTextMarkdownWriter::~QTextMarkdownWriter()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextMarkdownWriterD1Ev(QTextMarkdownWriter *self) {
  delete self;
}

//  a QTextMarkdownWriter::ListInfo a ritual of QTextMarkdownWriter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTextMarkdownWriter__QTextMarkdownWriter_ListInfo(
    QTextMarkdownWriter::ListInfo *self) {
  delete self;
}

#endif  // QT_CONFIG(textmarkdownwriter)
