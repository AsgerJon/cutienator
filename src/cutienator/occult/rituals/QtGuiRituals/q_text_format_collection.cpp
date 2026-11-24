//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextformat_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextformat_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtextformat.h>
#include <QtGui/qfont.h>

//  QTextFormatCollection::QTextFormatCollection()
extern "C" Q_DECL_EXPORT
QTextFormatCollection *ritual_ZN21QTextFormatCollectionC1Ev() {
  return new QTextFormatCollection();
}

//  QTextFormatCollection::~QTextFormatCollection()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTextFormatCollectionD1Ev(QTextFormatCollection *self) {
  delete self;
}

//  void QTextFormatCollection::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTextFormatCollection5clearEv(QTextFormatCollection *self) {
  self->clear();
}

//  QTextFormat QTextFormatCollection::objectFormat(int objectIndex) const
extern "C" Q_DECL_EXPORT
QTextFormat *ritual_ZNK21QTextFormatCollection12objectFormatEi(
    const QTextFormatCollection *self,
    int objectIndex) {
  return new QTextFormat(self->objectFormat(objectIndex));
}

//  void QTextFormatCollection::setObjectFormat(int objectIndex, const
//      QTextFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTextFormatCollection15setObjectFormatEiRK11QTextFormat(
    QTextFormatCollection *self,
    int objectIndex,
    const QTextFormat *format) {
  self->setObjectFormat(objectIndex, *format);
}

//  int QTextFormatCollection::objectFormatIndex(int objectIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QTextFormatCollection17objectFormatIndexEi(
    const QTextFormatCollection *self,
    int objectIndex) {
  return self->objectFormatIndex(objectIndex);
}

//  void QTextFormatCollection::setObjectFormatIndex(int objectIndex, int
//      formatIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTextFormatCollection20setObjectFormatIndexEii(
    QTextFormatCollection *self,
    int objectIndex,
    int formatIndex) {
  self->setObjectFormatIndex(objectIndex, formatIndex);
}

//  int QTextFormatCollection::createObjectIndex(const QTextFormat &f)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QTextFormatCollection17createObjectIndexERK11QTextFormat(
    QTextFormatCollection *self,
    const QTextFormat *f) {
  return self->createObjectIndex(*f);
}

//  int QTextFormatCollection::indexForFormat(const QTextFormat &f)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QTextFormatCollection14indexForFormatERK11QTextFormat(
    QTextFormatCollection *self,
    const QTextFormat *f) {
  return self->indexForFormat(*f);
}

//  bool QTextFormatCollection::hasFormatCached(const QTextFormat &format)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QTextFormatCollection15hasFormatCachedERK11QTextFormat(
    const QTextFormatCollection *self,
    const QTextFormat *format) {
  return self->hasFormatCached(*format);
}

//  QTextFormat QTextFormatCollection::format(int idx) const
extern "C" Q_DECL_EXPORT
QTextFormat *ritual_ZNK21QTextFormatCollection6formatEi(
    const QTextFormatCollection *self,
    int idx) {
  return new QTextFormat(self->format(idx));
}

//  QTextBlockFormat QTextFormatCollection::blockFormat(int index) const
extern "C" Q_DECL_EXPORT
QTextBlockFormat *ritual_ZNK21QTextFormatCollection11blockFormatEi(
    const QTextFormatCollection *self,
    int index) {
  return new QTextBlockFormat(self->blockFormat(index));
}

//  QTextCharFormat QTextFormatCollection::charFormat(int index) const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK21QTextFormatCollection10charFormatEi(
    const QTextFormatCollection *self,
    int index) {
  return new QTextCharFormat(self->charFormat(index));
}

//  QTextListFormat QTextFormatCollection::listFormat(int index) const
extern "C" Q_DECL_EXPORT
QTextListFormat *ritual_ZNK21QTextFormatCollection10listFormatEi(
    const QTextFormatCollection *self,
    int index) {
  return new QTextListFormat(self->listFormat(index));
}

//  QTextTableFormat QTextFormatCollection::tableFormat(int index) const
extern "C" Q_DECL_EXPORT
QTextTableFormat *ritual_ZNK21QTextFormatCollection11tableFormatEi(
    const QTextFormatCollection *self,
    int index) {
  return new QTextTableFormat(self->tableFormat(index));
}

//  QTextImageFormat QTextFormatCollection::imageFormat(int index) const
extern "C" Q_DECL_EXPORT
QTextImageFormat *ritual_ZNK21QTextFormatCollection11imageFormatEi(
    const QTextFormatCollection *self,
    int index) {
  return new QTextImageFormat(self->imageFormat(index));
}

//  int QTextFormatCollection::numFormats() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QTextFormatCollection10numFormatsEv(
    const QTextFormatCollection *self) {
  return self->numFormats();
}

//  QFont QTextFormatCollection::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK21QTextFormatCollection11defaultFontEv(
    const QTextFormatCollection *self) {
  return new QFont(self->defaultFont());
}

//  void QTextFormatCollection::setDefaultFont(const QFont &f)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTextFormatCollection14setDefaultFontERK5QFont(
    QTextFormatCollection *self,
    const QFont *f) {
  self->setDefaultFont(*f);
}

//  void QTextFormatCollection::setSuperScriptBaseline(qreal baseline)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTextFormatCollection22setSuperScriptBaselineEd(
    QTextFormatCollection *self,
    qreal baseline) {
  self->setSuperScriptBaseline(baseline);
}

//  void QTextFormatCollection::setSubScriptBaseline(qreal baseline)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTextFormatCollection20setSubScriptBaselineEd(
    QTextFormatCollection *self,
    qreal baseline) {
  self->setSubScriptBaseline(baseline);
}

//  void QTextFormatCollection::setBaselineOffset(qreal baseline)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTextFormatCollection17setBaselineOffsetEd(
    QTextFormatCollection *self,
    qreal baseline) {
  self->setBaselineOffset(baseline);
}

//  QTextCharFormat QTextFormatCollection::defaultTextFormat() const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK21QTextFormatCollection17defaultTextFormatEv(
    const QTextFormatCollection *self) {
  return new QTextCharFormat(self->defaultTextFormat());
}
