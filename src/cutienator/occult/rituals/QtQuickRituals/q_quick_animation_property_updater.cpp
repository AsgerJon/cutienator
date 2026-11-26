//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickanimation_p.h>
#include <QtQuick/private/qquickanimation_p_p.h>
#include <QtQuick/private/qquickanimatorjob_p.h>
#include <QtQuick/private/qquickstatechangescript_p.h>
#include <QtQml/private/qqmlcontext_p.h>
#include <QtQml/qqmlpropertyvaluesource.h>
#include <QtQml/qqml.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlexpression.h>
#include <QtQml/private/qqmlstringconverters_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlmetatype_p.h>
#include <QtQml/private/qqmlvaluetype_p.h>
#include <QtQml/private/qqmlproperty_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtCore/qvariant.h>
#include <QtGui/qcolor.h>
#include <QtCore/qfile.h>
#include <QtQml/private/qparallelanimationgroupjob_p.h>
#include <QtQml/private/qsequentialanimationgroupjob_p.h>
#include <QtCore/qset.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qmath.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 2704, as _ZN30QQuickAnimationPropertyUpdater8setValueEd
inline void QQuickAnimationPropertyUpdater::setValue(qreal v)
{
    bool deleted = false;
    wasDeleted = &deleted;
    if (reverse)
        v = 1 - v;
    for (int ii = 0; ii < actions.size(); ++ii) {
        QQuickStateAction &action = actions[ii];

        if (v == qreal(1.0) && extendedInterpolator == nullptr) {
            QQmlPropertyPrivate::write(action.property, action.toValue, QQmlPropertyData::BypassInterceptor | QQmlPropertyData::DontRemoveBinding);
        } else {
            if (!fromIsSourced && !fromIsDefined) {
                action.fromValue = action.property.read();
                if (interpolatorType) {
                    QQuickPropertyAnimationPrivate::convertVariant(action.fromValue, QMetaType(interpolatorType));
                }
            }
            if (!interpolatorType) {
                int propType = action.property.propertyType();
                if (!prevInterpolatorType || prevInterpolatorType != propType) {
                    prevInterpolatorType = propType;
                    interpolator = QVariantAnimationPrivate::getInterpolator(prevInterpolatorType);
                }
            }

            QVariant interpolated;
            if (extendedInterpolator) {
                QVariant current = action.property.read();
                interpolated = extendedInterpolator(action.fromValue.constData(),
                                                    action.toValue.constData(),
                                                    current,
                                                    v);

            } else if (interpolator) {
                interpolated = interpolator(action.fromValue.constData(), action.toValue.constData(), v);
            }
            QQmlPropertyPrivate::write(action.property,
                                       interpolated,
                                       QQmlPropertyData::BypassInterceptor | QQmlPropertyData::DontRemoveBinding);
        }
        if (deleted)
            return;
    }
    wasDeleted = nullptr;
    fromIsSourced = true;
}

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 2910, as _ZN30QQuickAnimationPropertyUpdaterD2Ev
inline QQuickAnimationPropertyUpdater::~QQuickAnimationPropertyUpdater()
{
    if (wasDeleted) *wasDeleted = true;
}

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 2752, as _ZNK30QQuickAnimationPropertyUpdater12debugUpdaterE6QDebugi
inline void QQuickAnimationPropertyUpdater::debugUpdater(QDebug d, int indentLevel) const
{
    QByteArray ind(indentLevel, ' ');
    for (int i = 0; i < actions.size(); ++i) {
        const QQuickStateAction &action = actions.at(i);
        d << "\n" << ind.constData() << "target:" << action.property.object() << "property:" << action.property.name()
          << "from:" << action.fromValue << "to:" << action.toValue;
    }
}
//  -----------------------------------------------------------------------

//  A QQuickAnimationPropertyUpdater that Python can take functions over in. Every QQuickAnimationPropertyUpdater
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickAnimationPropertyUpdaterCall0)(const void *, qreal, int *);
typedef void (*CuteQQuickAnimationPropertyUpdaterCall1)(const void *, const QDebug *, int, int *);
class CuteQQuickAnimationPropertyUpdater : public QQuickAnimationPropertyUpdater {
public:
  using QQuickAnimationPropertyUpdater::QQuickAnimationPropertyUpdater;
  CuteQQuickAnimationPropertyUpdater(const QQuickAnimationPropertyUpdater & other) : QQuickAnimationPropertyUpdater(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QQuickBulkValueUpdater8setValueEd")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QQuickBulkValueUpdater12debugUpdaterE6QDebugi")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QQuickAnimationPropertyUpdater::setValue(qreal v)
  void setValue(qreal v) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAnimationPropertyUpdaterCall0 call = reinterpret_cast<CuteQQuickAnimationPropertyUpdaterCall0>(taken[0]);
      call(this, v, &handled);
      if (handled) return;
    }
    QQuickAnimationPropertyUpdater::setValue(v);
  }

  //  void QQuickAnimationPropertyUpdater::debugUpdater(QDebug d, int
  //      indentLevel) const
  void debugUpdater(QDebug d, int indentLevel) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAnimationPropertyUpdaterCall1 call = reinterpret_cast<CuteQQuickAnimationPropertyUpdaterCall1>(taken[1]);
      call(this, &d, indentLevel, &handled);
      if (handled) return;
    }
    QQuickAnimationPropertyUpdater::debugUpdater(d, indentLevel);
  }
};

//  QQuickAnimationPropertyUpdater::QQuickAnimationPropertyUpdater()
extern "C" Q_DECL_EXPORT
QQuickAnimationPropertyUpdater *ritual_ZN30QQuickAnimationPropertyUpdaterC1Ev() {
  return new CuteQQuickAnimationPropertyUpdater();
}

//  QQuickAnimationPropertyUpdater::~QQuickAnimationPropertyUpdater()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickAnimationPropertyUpdaterD1Ev(
    QQuickAnimationPropertyUpdater *self) {
  delete self;
}

//  void QQuickAnimationPropertyUpdater::setValue(qreal v)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickAnimationPropertyUpdater8setValueEd(
    QQuickAnimationPropertyUpdater *self,
    qreal v) {
  self->setValue(v);
}

//  void QQuickAnimationPropertyUpdater::debugUpdater(QDebug d, int
//      indentLevel) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK30QQuickAnimationPropertyUpdater12debugUpdaterE6QDebugi(
    const QQuickAnimationPropertyUpdater *self,
    const QDebug *d,
    int indentLevel) {
  self->debugUpdater(*d, indentLevel);
}

//  a Python function taken by a CuteQQuickAnimationPropertyUpdater, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAnimationPropertyUpdater(
    QQuickAnimationPropertyUpdater *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAnimationPropertyUpdater *>(self)->take(key, call);
}

//  void QQuickAnimationPropertyUpdater::setValue(qreal v)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuickAnimationPropertyUpdater8setValueEd(
    QQuickAnimationPropertyUpdater *self,
    qreal v) {
  self->QQuickAnimationPropertyUpdater::setValue(v);
}

//  void QQuickAnimationPropertyUpdater::debugUpdater(QDebug d, int
//      indentLevel) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK30QQuickAnimationPropertyUpdater12debugUpdaterE6QDebugi(
    const QQuickAnimationPropertyUpdater *self,
    const QDebug *d,
    int indentLevel) {
  self->QQuickAnimationPropertyUpdater::debugUpdater(*d, indentLevel);
}
