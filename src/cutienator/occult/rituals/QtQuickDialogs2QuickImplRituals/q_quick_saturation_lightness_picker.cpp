//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquicksaturationlightn
//  esspicker_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquicksaturationlightnesspicker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtGui/qcolor.h>

//  Only a class built on QQuickSaturationLightnessPicker may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickSaturationLightnessPicker : QQuickSaturationLightnessPicker {
  using QQuickSaturationLightnessPicker::colorAt;
};

//  const QMetaObject *QQuickSaturationLightnessPicker::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QQuickSaturationLightnessPicker10metaObjectEv(
    const QQuickSaturationLightnessPicker *self) {
  return self->metaObject();
}

//  void *QQuickSaturationLightnessPicker::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN31QQuickSaturationLightnessPicker11qt_metacastEPKc(
    QQuickSaturationLightnessPicker *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickSaturationLightnessPicker::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN31QQuickSaturationLightnessPicker11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickSaturationLightnessPicker *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickSaturationLightnessPicker::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QQuickSaturationLightnessPicker2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSaturationLightnessPicker::tr(s, c, n));
}

//  QQuickSaturationLightnessPicker::QQuickSaturationLightnessPicker(QQuickIt
//      em *parent)
extern "C" Q_DECL_EXPORT
QQuickSaturationLightnessPicker *ritual_ZN31QQuickSaturationLightnessPickerC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickSaturationLightnessPicker(parent);
}

//  QColor QQuickSaturationLightnessPicker::colorAt(const QPointF &pos)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN31QQuickSaturationLightnessPicker7colorAtERK7QPointF(
    QQuickSaturationLightnessPicker *self,
    const QPointF *pos) {
  return new QColor(self->colorAt(*pos));
}

//  QQuickSaturationLightnessPickerPrivate
//      *QQuickSaturationLightnessPicker::d_func()
extern "C" Q_DECL_EXPORT
QQuickSaturationLightnessPickerPrivate *ritual_ZN31QQuickSaturationLightnessPicker6d_funcEv(
    QQuickSaturationLightnessPicker *self) {
  return self->d_func();
}

//  const QQuickSaturationLightnessPickerPrivate
//      *QQuickSaturationLightnessPicker::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickSaturationLightnessPickerPrivate *ritual_ZNK31QQuickSaturationLightnessPicker6d_funcEv(
    const QQuickSaturationLightnessPicker *self) {
  return self->d_func();
}

//  QColor QQuickSaturationLightnessPicker::colorAt(const QPointF &pos)
extern "C" Q_DECL_EXPORT
QColor *ritual_own_ZN31QQuickSaturationLightnessPicker7colorAtERK7QPointF(
    QQuickSaturationLightnessPicker *self,
    const QPointF *pos) {
  return new QColor(
      static_cast<OwnQQuickSaturationLightnessPicker *>(self)->OwnQQuickSaturationLightnessPicker::colorAt(
          *pos));
}
