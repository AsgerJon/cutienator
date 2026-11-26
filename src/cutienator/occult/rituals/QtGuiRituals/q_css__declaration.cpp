//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcssparser_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(cssparser)
#if !defined(QT_NO_CSSPARSER)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcssparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpalette.h>
#include <QtGui/qcolor.h>
#include <QtGui/qbrush.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtCore/QList>

//  QCss::Declaration::Declaration()
extern "C" Q_DECL_EXPORT
QCss::Declaration *ritual_ZN4QCss11DeclarationC1Ev() {
  return new QCss::Declaration();
}

//  bool QCss::Declaration::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QCss11Declaration7isEmptyEv(const QCss::Declaration *self) {
  return self->isEmpty();
}

//  QColor QCss::Declaration::colorValue(const QPalette &a0) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK4QCss11Declaration10colorValueERK8QPalette(
    const QCss::Declaration *self,
    const QPalette *a0) {
  return new QColor(self->colorValue(*a0));
}

//  void QCss::Declaration::colorValues(QColor *c, const QPalette &a1) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QCss11Declaration11colorValuesEP6QColorRK8QPalette(
    const QCss::Declaration *self,
    QColor *c,
    const QPalette *a1) {
  self->colorValues(c, *a1);
}

//  QBrush QCss::Declaration::brushValue(const QPalette &a0) const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK4QCss11Declaration10brushValueERK8QPalette(
    const QCss::Declaration *self,
    const QPalette *a0) {
  return new QBrush(self->brushValue(*a0));
}

//  void QCss::Declaration::brushValues(QBrush *c, const QPalette &a1) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QCss11Declaration11brushValuesEP6QBrushRK8QPalette(
    const QCss::Declaration *self,
    QBrush *c,
    const QPalette *a1) {
  self->brushValues(c, *a1);
}

//  BorderStyle QCss::Declaration::styleValue() const
extern "C" Q_DECL_EXPORT
QCss::BorderStyle ritual_ZNK4QCss11Declaration10styleValueEv(
    const QCss::Declaration *self) {
  return self->styleValue();
}

//  void QCss::Declaration::styleValues(BorderStyle *s) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QCss11Declaration11styleValuesEPNS_11BorderStyleE(
    const QCss::Declaration *self,
    QCss::BorderStyle *s) {
  self->styleValues(s);
}

//  Origin QCss::Declaration::originValue() const
extern "C" Q_DECL_EXPORT
QCss::Origin ritual_ZNK4QCss11Declaration11originValueEv(
    const QCss::Declaration *self) {
  return self->originValue();
}

//  Repeat QCss::Declaration::repeatValue() const
extern "C" Q_DECL_EXPORT
QCss::Repeat ritual_ZNK4QCss11Declaration11repeatValueEv(
    const QCss::Declaration *self) {
  return self->repeatValue();
}

//  Qt::Alignment QCss::Declaration::alignmentValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK4QCss11Declaration14alignmentValueEv(
    const QCss::Declaration *self) {
  return static_cast<int>(self->alignmentValue().toInt());
}

//  PositionMode QCss::Declaration::positionValue() const
extern "C" Q_DECL_EXPORT
QCss::PositionMode ritual_ZNK4QCss11Declaration13positionValueEv(
    const QCss::Declaration *self) {
  return self->positionValue();
}

//  Attachment QCss::Declaration::attachmentValue() const
extern "C" Q_DECL_EXPORT
QCss::Attachment ritual_ZNK4QCss11Declaration15attachmentValueEv(
    const QCss::Declaration *self) {
  return self->attachmentValue();
}

//  int QCss::Declaration::styleFeaturesValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK4QCss11Declaration18styleFeaturesValueEv(
    const QCss::Declaration *self) {
  return self->styleFeaturesValue();
}

//  bool QCss::Declaration::intValue(int *i, const char *unit) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QCss11Declaration8intValueEPiPKc(
    const QCss::Declaration *self,
    int *i,
    const char *unit) {
  return self->intValue(i, unit);
}

//  bool QCss::Declaration::realValue(qreal *r, const char *unit) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QCss11Declaration9realValueEPdPKc(
    const QCss::Declaration *self,
    qreal *r,
    const char *unit) {
  return self->realValue(r, unit);
}

//  QSize QCss::Declaration::sizeValue() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK4QCss11Declaration9sizeValueEv(
    const QCss::Declaration *self) {
  return new QSize(self->sizeValue());
}

//  QRect QCss::Declaration::rectValue() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK4QCss11Declaration9rectValueEv(
    const QCss::Declaration *self) {
  return new QRect(self->rectValue());
}

//  QString QCss::Declaration::uriValue() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QCss11Declaration8uriValueEv(
    const QCss::Declaration *self) {
  return new QString(self->uriValue());
}

//  QIcon QCss::Declaration::iconValue() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK4QCss11Declaration9iconValueEv(
    const QCss::Declaration *self) {
  return new QIcon(self->iconValue());
}

//  void QCss::Declaration::borderImageValue(QString *image, int *cuts,
//      TileMode *h, TileMode *v) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QCss11Declaration16borderImageValueEP7QStringPiPNS_8TileModeES5_(
    const QCss::Declaration *self,
    QString *image,
    int *cuts,
    QCss::TileMode *h,
    QCss::TileMode *v) {
  self->borderImageValue(image, cuts, h, v);
}

//  bool QCss::Declaration::borderCollapseValue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QCss11Declaration19borderCollapseValueEv(
    const QCss::Declaration *self) {
  return self->borderCollapseValue();
}

//  QList<qreal> QCss::Declaration::dashArray() const
extern "C" Q_DECL_EXPORT
QList<qreal> *ritual_ZNK4QCss11Declaration9dashArrayEv(
    const QCss::Declaration *self) {
  return new QList<qreal>(self->dashArray());
}

//  QCss::Declaration::~Declaration()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QCss11DeclarationD1Ev(QCss::Declaration *self) {
  delete self;
}

//  a QList<qreal> a ritual of QCss::Declaration gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QCss_Declaration__QList_qreal(QList<qreal> *self) {
  delete self;
}

#endif  // !defined(QT_NO_CSSPARSER)
#endif  // QT_CONFIG(cssparser)
