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

//  QColor QQuickSaturationLightnessPicker::colorAt(const QPointF &pos)
extern "C" Q_DECL_EXPORT
QColor *ritual_own_ZN31QQuickSaturationLightnessPicker7colorAtERK7QPointF(
    QQuickSaturationLightnessPicker *self,
    const QPointF *pos) {
  return new QColor(
      static_cast<OwnQQuickSaturationLightnessPicker *>(self)->OwnQQuickSaturationLightnessPicker::colorAt(
          *pos));
}
