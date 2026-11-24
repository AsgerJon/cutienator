//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextmarkdownimporter_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(textmarkdownreader)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextmarkdownimporter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QTextMarkdownImporter::QTextMarkdownImporter(QTextDocument *doc, Features
//      features)
extern "C" Q_DECL_EXPORT
QTextMarkdownImporter *ritual_ZN21QTextMarkdownImporterC1EP13QTextDocument6QFlagsINS_7FeatureEE(
    QTextDocument *doc,
    int features) {
  return new QTextMarkdownImporter(
      doc,
      QFlags<QTextMarkdownImporter::Feature>::fromInt(features));
}

//  QTextMarkdownImporter::QTextMarkdownImporter(QTextDocument *doc,
//      QTextDocument::MarkdownFeatures features)
extern "C" Q_DECL_EXPORT
QTextMarkdownImporter *ritual_ZN21QTextMarkdownImporterC1EP13QTextDocument6QFlagsINS0_15MarkdownFeatureEE(
    QTextDocument *doc,
    int features) {
  return new QTextMarkdownImporter(
      doc,
      QFlags<QTextDocument::MarkdownFeature>::fromInt(features));
}

//  void QTextMarkdownImporter::import(const QString &markdown)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTextMarkdownImporter6importERK7QString(
    QTextMarkdownImporter *self,
    const QString *markdown) {
  self->import(*markdown);
}

//  int QTextMarkdownImporter::cbText(int textType, const char *text,
//      unsigned int size)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QTextMarkdownImporter6cbTextEiPKcj(
    QTextMarkdownImporter *self,
    int textType,
    const char *text,
    unsigned int size) {
  return self->cbText(textType, text, size);
}

//  void QTextMarkdownImporter::insertBlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTextMarkdownImporter11insertBlockEv(
    QTextMarkdownImporter *self) {
  self->insertBlock();
}

//  QTextMarkdownImporter::~QTextMarkdownImporter()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTextMarkdownImporterD1Ev(QTextMarkdownImporter *self) {
  delete self;
}

#endif  // QT_CONFIG(textmarkdownreader)
