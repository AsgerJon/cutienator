//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qstatictext.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qstatictext.h>
#include <QtCore/qstring.h>
#include <QtGui/qtextoption.h>
#include <QtCore/qsize.h>
#include <QtGui/qtransform.h>
#include <QtGui/qfont.h>

//  QStaticText::QStaticText()
extern "C" Q_DECL_EXPORT
QStaticText *ritual_ZN11QStaticTextC1Ev() {
  return new QStaticText();
}

//  QStaticText::QStaticText(const QString &text)
extern "C" Q_DECL_EXPORT
QStaticText *ritual_ZN11QStaticTextC1ERK7QString(const QString *text) {
  return new QStaticText(*text);
}

//  QStaticText::QStaticText(const QStaticText &other)
extern "C" Q_DECL_EXPORT
QStaticText *ritual_ZN11QStaticTextC1ERKS_(const QStaticText *other) {
  return new QStaticText(*other);
}

//  QStaticText &QStaticText::operator=(QStaticText &&other)
extern "C" Q_DECL_EXPORT
QStaticText *ritual_ZN11QStaticTextaSEOS_(
    QStaticText *self,
    QStaticText *other) {
  return &(self->operator=(std::move(*other)));
}

//  QStaticText &QStaticText::operator=(const QStaticText &a0)
extern "C" Q_DECL_EXPORT
QStaticText *ritual_ZN11QStaticTextaSERKS_(
    QStaticText *self,
    const QStaticText *a0) {
  return &(self->operator=(*a0));
}

//  QStaticText::~QStaticText()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStaticTextD1Ev(QStaticText *self) {
  delete self;
}

//  void QStaticText::swap(QStaticText &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStaticText4swapERS_(QStaticText *self, QStaticText *other) {
  self->swap(*other);
}

//  void QStaticText::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStaticText7setTextERK7QString(
    QStaticText *self,
    const QString *text) {
  self->setText(*text);
}

//  QString QStaticText::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QStaticText4textEv(const QStaticText *self) {
  return new QString(self->text());
}

//  void QStaticText::setTextFormat(Qt::TextFormat textFormat)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStaticText13setTextFormatEN2Qt10TextFormatE(
    QStaticText *self,
    Qt::TextFormat textFormat) {
  self->setTextFormat(textFormat);
}

//  Qt::TextFormat QStaticText::textFormat() const
extern "C" Q_DECL_EXPORT
Qt::TextFormat ritual_ZNK11QStaticText10textFormatEv(
    const QStaticText *self) {
  return self->textFormat();
}

//  void QStaticText::setTextWidth(qreal textWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStaticText12setTextWidthEd(
    QStaticText *self,
    qreal textWidth) {
  self->setTextWidth(textWidth);
}

//  qreal QStaticText::textWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QStaticText9textWidthEv(const QStaticText *self) {
  return self->textWidth();
}

//  void QStaticText::setTextOption(const QTextOption &textOption)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStaticText13setTextOptionERK11QTextOption(
    QStaticText *self,
    const QTextOption *textOption) {
  self->setTextOption(*textOption);
}

//  QTextOption QStaticText::textOption() const
extern "C" Q_DECL_EXPORT
QTextOption *ritual_ZNK11QStaticText10textOptionEv(const QStaticText *self) {
  return new QTextOption(self->textOption());
}

//  QSizeF QStaticText::size() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK11QStaticText4sizeEv(const QStaticText *self) {
  return new QSizeF(self->size());
}

//  void QStaticText::prepare(const QTransform &matrix, const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStaticText7prepareERK10QTransformRK5QFont(
    QStaticText *self,
    const QTransform *matrix,
    const QFont *font) {
  self->prepare(*matrix, *font);
}

//  void QStaticText::setPerformanceHint(PerformanceHint performanceHint)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStaticText18setPerformanceHintENS_15PerformanceHintE(
    QStaticText *self,
    QStaticText::PerformanceHint performanceHint) {
  self->setPerformanceHint(performanceHint);
}

//  PerformanceHint QStaticText::performanceHint() const
extern "C" Q_DECL_EXPORT
QStaticText::PerformanceHint ritual_ZNK11QStaticText15performanceHintEv(
    const QStaticText *self) {
  return self->performanceHint();
}

//  bool QStaticText::operator==(const QStaticText &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStaticTexteqERKS_(
    const QStaticText *self,
    const QStaticText *a0) {
  return self->operator==(*a0);
}

//  bool QStaticText::operator!=(const QStaticText &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStaticTextneERKS_(
    const QStaticText *self,
    const QStaticText *a0) {
  return self->operator!=(*a0);
}

//  void QStaticText::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStaticText6detachEv(QStaticText *self) {
  self->detach();
}
