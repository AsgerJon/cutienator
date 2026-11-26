//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickcolordialogimpl_
//  p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickcolordialogimpl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/QSharedPointer>

//  const QMetaObject *QQuickColorDialogImpl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickColorDialogImpl10metaObjectEv(
    const QQuickColorDialogImpl *self) {
  return self->metaObject();
}

//  void *QQuickColorDialogImpl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuickColorDialogImpl11qt_metacastEPKc(
    QQuickColorDialogImpl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickColorDialogImpl::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuickColorDialogImpl11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickColorDialogImpl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickColorDialogImpl::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickColorDialogImpl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickColorDialogImpl::tr(s, c, n));
}

//  void QQuickColorDialogImpl::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickColorDialogImpl21qt_qmlMarker_attachedEv(
    QQuickColorDialogImpl *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickColorDialogImpl::QQuickColorDialogImpl(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickColorDialogImpl *ritual_ZN21QQuickColorDialogImplC1EP7QObject(
    QObject *parent) {
  return new QQuickColorDialogImpl(parent);
}

//  QQuickColorDialogImplAttached
//      *QQuickColorDialogImpl::qmlAttachedProperties(QObject *object)
extern "C" Q_DECL_EXPORT
QQuickColorDialogImplAttached *ritual_ZN21QQuickColorDialogImpl21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickColorDialogImpl::qmlAttachedProperties(object);
}

//  QSharedPointer<QColorDialogOptions> QQuickColorDialogImpl::options()
//      const
extern "C" Q_DECL_EXPORT
QSharedPointer<QColorDialogOptions> *ritual_ZNK21QQuickColorDialogImpl7optionsEv(
    const QQuickColorDialogImpl *self) {
  return new QSharedPointer<QColorDialogOptions>(self->options());
}

//  void QQuickColorDialogImpl::setOptions(const
//      QSharedPointer<QColorDialogOptions> &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickColorDialogImpl10setOptionsERK14QSharedPointerI19QColorDialogOptionsE(
    QQuickColorDialogImpl *self,
    const QSharedPointer<QColorDialogOptions> *options) {
  self->setOptions(*options);
}

//  QColor QQuickColorDialogImpl::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK21QQuickColorDialogImpl5colorEv(
    const QQuickColorDialogImpl *self) {
  return new QColor(self->color());
}

//  void QQuickColorDialogImpl::setColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickColorDialogImpl8setColorERK6QColor(
    QQuickColorDialogImpl *self,
    const QColor *c) {
  self->setColor(*c);
}

//  int QQuickColorDialogImpl::red() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickColorDialogImpl3redEv(
    const QQuickColorDialogImpl *self) {
  return self->red();
}

//  void QQuickColorDialogImpl::setRed(int red)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickColorDialogImpl6setRedEi(
    QQuickColorDialogImpl *self,
    int red) {
  self->setRed(red);
}

//  int QQuickColorDialogImpl::green() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickColorDialogImpl5greenEv(
    const QQuickColorDialogImpl *self) {
  return self->green();
}

//  void QQuickColorDialogImpl::setGreen(int green)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickColorDialogImpl8setGreenEi(
    QQuickColorDialogImpl *self,
    int green) {
  self->setGreen(green);
}

//  int QQuickColorDialogImpl::blue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickColorDialogImpl4blueEv(
    const QQuickColorDialogImpl *self) {
  return self->blue();
}

//  void QQuickColorDialogImpl::setBlue(int blue)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickColorDialogImpl7setBlueEi(
    QQuickColorDialogImpl *self,
    int blue) {
  self->setBlue(blue);
}

//  qreal QQuickColorDialogImpl::alpha() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickColorDialogImpl5alphaEv(
    const QQuickColorDialogImpl *self) {
  return self->alpha();
}

//  void QQuickColorDialogImpl::setAlpha(qreal alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickColorDialogImpl8setAlphaEd(
    QQuickColorDialogImpl *self,
    qreal alpha) {
  self->setAlpha(alpha);
}

//  qreal QQuickColorDialogImpl::hue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickColorDialogImpl3hueEv(
    const QQuickColorDialogImpl *self) {
  return self->hue();
}

//  void QQuickColorDialogImpl::setHue(qreal hue)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickColorDialogImpl6setHueEd(
    QQuickColorDialogImpl *self,
    qreal hue) {
  self->setHue(hue);
}

//  qreal QQuickColorDialogImpl::saturation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickColorDialogImpl10saturationEv(
    const QQuickColorDialogImpl *self) {
  return self->saturation();
}

//  void QQuickColorDialogImpl::setSaturation(qreal saturation)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickColorDialogImpl13setSaturationEd(
    QQuickColorDialogImpl *self,
    qreal saturation) {
  self->setSaturation(saturation);
}

//  qreal QQuickColorDialogImpl::value() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickColorDialogImpl5valueEv(
    const QQuickColorDialogImpl *self) {
  return self->value();
}

//  void QQuickColorDialogImpl::setValue(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickColorDialogImpl8setValueEd(
    QQuickColorDialogImpl *self,
    qreal value) {
  self->setValue(value);
}

//  qreal QQuickColorDialogImpl::lightness() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickColorDialogImpl9lightnessEv(
    const QQuickColorDialogImpl *self) {
  return self->lightness();
}

//  void QQuickColorDialogImpl::setLightness(qreal lightness)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickColorDialogImpl12setLightnessEd(
    QQuickColorDialogImpl *self,
    qreal lightness) {
  self->setLightness(lightness);
}

//  bool QQuickColorDialogImpl::isHsl() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickColorDialogImpl5isHslEv(
    const QQuickColorDialogImpl *self) {
  return self->isHsl();
}

//  void QQuickColorDialogImpl::setHsl(bool hsl)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickColorDialogImpl6setHslEb(
    QQuickColorDialogImpl *self,
    bool hsl) {
  self->setHsl(hsl);
}

//  void QQuickColorDialogImpl::invokeEyeDropper()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickColorDialogImpl16invokeEyeDropperEv(
    QQuickColorDialogImpl *self) {
  self->invokeEyeDropper();
}

//  void QQuickColorDialogImpl::colorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickColorDialogImpl12colorChangedERK6QColor(
    QQuickColorDialogImpl *self,
    const QColor *color) {
  self->colorChanged(*color);
}

//  void QQuickColorDialogImpl::specChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickColorDialogImpl11specChangedEv(
    QQuickColorDialogImpl *self) {
  self->specChanged();
}

//  void QQuickColorDialogImpl::itemChange(QQuickItem::ItemChange change,
//      const QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickColorDialogImpl10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickColorDialogImpl *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  QQuickColorDialogImplPrivate *QQuickColorDialogImpl::d_func()
extern "C" Q_DECL_EXPORT
QQuickColorDialogImplPrivate *ritual_ZN21QQuickColorDialogImpl6d_funcEv(
    QQuickColorDialogImpl *self) {
  return self->d_func();
}

//  const QQuickColorDialogImplPrivate *QQuickColorDialogImpl::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickColorDialogImplPrivate *ritual_ZNK21QQuickColorDialogImpl6d_funcEv(
    const QQuickColorDialogImpl *self) {
  return self->d_func();
}

//  void QQuickColorDialogImpl::itemChange(QQuickItem::ItemChange change,
//      const QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickColorDialogImpl10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickColorDialogImpl *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->QQuickColorDialogImpl::itemChange(change, *data);
}

//  a QSharedPointer<QColorDialogOptions> a ritual of QQuickColorDialogImpl
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickColorDialogImpl__QSharedPointer_QColorDialogOptions(
    QSharedPointer<QColorDialogOptions> *self) {
  delete self;
}
