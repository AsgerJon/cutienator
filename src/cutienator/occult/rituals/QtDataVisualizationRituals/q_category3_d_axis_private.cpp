//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/qcategory3daxis_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QCategory3DAxisPrivate'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 2 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/qcategory3daxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtDataVisualization/private/qabstract3daxis_p.h>
#include <QtDataVisualization/private/qcategory3daxis_p.h>
#include <QtDataVisualization/private/bars3dcontroller_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtDataVisualization__QCategory3DAxisPrivate.cpp, line 1, as moc:QCategory3DAxisPrivate
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN22QCategory3DAxisPrivateE_t {};
} // unnamed namespace

template <> constexpr inline auto QCategory3DAxisPrivate::qt_create_metaobjectdata<qt_meta_tag_ZN22QCategory3DAxisPrivateE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QCategory3DAxisPrivate"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QCategory3DAxisPrivate, qt_meta_tag_ZN22QCategory3DAxisPrivateE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QCategory3DAxisPrivate::staticMetaObject = { {
    QMetaObject::SuperData::link<QAbstract3DAxisPrivate::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QCategory3DAxisPrivateE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QCategory3DAxisPrivateE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN22QCategory3DAxisPrivateE_t>.metaTypes,
    nullptr
} };

void QCategory3DAxisPrivate::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QCategory3DAxisPrivate *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QCategory3DAxisPrivate::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QCategory3DAxisPrivate::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN22QCategory3DAxisPrivateE_t>.strings))
        return static_cast<void*>(this);
    return QAbstract3DAxisPrivate::qt_metacast(_clname);
}

int QCategory3DAxisPrivate::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QAbstract3DAxisPrivate::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtdatavis3d/src/datavisualization/axis/qabstract3daxis.cpp, line 403, as _ZN22QAbstract3DAxisPrivate12updateLabelsEv
inline void QAbstract3DAxisPrivate::updateLabels()
{
    // Default implementation does nothing
}

//  from ../qtdatavis3d/src/datavisualization/axis/qabstract3daxis.cpp, line 503, as _ZN22QAbstract3DAxisPrivate6setMaxEf
inline void QAbstract3DAxisPrivate::setMax(float max)
{
    if (!allowNegatives()) {
        if (allowZero()) {
            if (max < 0.0f) {
                max = 0.0f;
                qWarning() << "Warning: Tried to set negative maximum for an axis that only"
                              "supports positive values and zero:" << max;
            }
        } else {
            if (max <= 0.0f) {
                max = 1.0f;
                qWarning() << "Warning: Tried to set negative or zero maximum for an axis that only"
                              "supports positive values:" << max;
            }
        }
    }

    if (m_max != max) {
        bool minChanged = false;
        if (m_min > max || (!allowMinMaxSame() && m_min == max)) {
            float oldMin = m_min;
            m_min = max - 1.0f;
            if (!allowNegatives() && m_min < 0.0f) {
                if (allowZero())
                    m_min = 0.0f;
                else
                    m_min = max / 2.0f; // Need some positive value smaller than max

                if (!allowMinMaxSame() && max == 0.0f) {
                    m_min = oldMin;
                    qWarning() << "Unable to set maximum value to zero.";
                    return;
                }
            }
            qWarning() << "Warning: Tried to set maximum to equal or smaller than minimum for"
                          " value axis. Minimum automatically adjusted to a valid one:"
                       << oldMin <<  "-->" << m_min;
            minChanged = true;
        }
        m_max = max;
        emit q_ptr->rangeChanged(m_min, m_max);
        emit q_ptr->maxChanged(m_max);
        if (minChanged)
            emit q_ptr->minChanged(m_min);
    }
}

//  from ../qtdatavis3d/src/datavisualization/axis/qabstract3daxis.cpp, line 466, as _ZN22QAbstract3DAxisPrivate6setMinEf
inline void QAbstract3DAxisPrivate::setMin(float min)
{
    if (!allowNegatives()) {
        if (allowZero()) {
            if (min < 0.0f) {
                min = 0.0f;
                qWarning() << "Warning: Tried to set negative minimum for an axis that only"
                              "supports positive values and zero:" << min;
            }
        } else {
            if (min <= 0.0f) {
                min = 1.0f;
                qWarning() << "Warning: Tried to set negative or zero minimum for an axis that only"
                              "supports positive values:" << min;
            }
        }
    }

    if (m_min != min) {
        bool maxChanged = false;
        if (min > m_max || (!allowMinMaxSame() && min == m_max)) {
            float oldMax = m_max;
            m_max = min + 1.0f;
            qWarning() << "Warning: Tried to set minimum to equal or larger than maximum for"
                          " value axis. Maximum automatically adjusted to a valid one:"
                       << oldMax <<  "-->" << m_max;
            maxChanged = true;
        }
        m_min = min;

        emit q_ptr->rangeChanged(m_min, m_max);
        emit q_ptr->minChanged(m_min);
        if (maxChanged)
            emit q_ptr->maxChanged(m_max);
    }
}

//  from ../qtdatavis3d/src/datavisualization/axis/qabstract3daxis.cpp, line 408, as _ZN22QAbstract3DAxisPrivate8setRangeEffb
inline void QAbstract3DAxisPrivate::setRange(float min, float max, bool suppressWarnings)
{
    bool adjusted = false;
    if (!allowNegatives()) {
        if (allowZero()) {
            if (min < 0.0f) {
                min = 0.0f;
                adjusted = true;
            }
            if (max < 0.0f) {
                max = 0.0f;
                adjusted = true;
            }
        } else {
            if (min <= 0.0f) {
                min = 1.0f;
                adjusted = true;
            }
            if (max <= 0.0f) {
                max = 1.0f;
                adjusted = true;
            }
        }
    }
    // If min >= max, we adjust ranges so that
    // m_max becomes (min + 1.0f)
    // as axes need some kind of valid range.
    bool minDirty = false;
    bool maxDirty = false;
    if (m_min != min) {
        m_min = min;
        minDirty = true;
    }
    if (m_max != max || min > max || (!allowMinMaxSame() && min == max)) {
        if (min > max || (!allowMinMaxSame() && min == max)) {
            m_max = min + 1.0f;
            adjusted = true;
        } else {
            m_max = max;
        }
        maxDirty = true;
    }

    if (minDirty || maxDirty) {
        if (adjusted && !suppressWarnings) {
            qWarning() << "Warning: Tried to set invalid range for axis."
                          " Range automatically adjusted to a valid one:"
                       << min << "-" << max << "-->" << m_min << "-" << m_max;
        }
        emit q_ptr->rangeChanged(m_min, m_max);
    }

    if (minDirty)
        emit q_ptr->minChanged(m_min);
    if (maxDirty)
        emit q_ptr->maxChanged(m_max);
}

//  from ../qtdatavis3d/src/datavisualization/axis/qcategory3daxis.cpp, line 133, as _ZN22QCategory3DAxisPrivate14allowNegativesEv
inline bool QCategory3DAxisPrivate::allowNegatives()
{
    return false;
}

//  from ../qtdatavis3d/src/datavisualization/axis/qcategory3daxis.cpp, line 138, as _ZN22QCategory3DAxisPrivate15allowMinMaxSameEv
inline bool QCategory3DAxisPrivate::allowMinMaxSame()
{
    return true;
}

//  from ../qtdatavis3d/src/datavisualization/axis/qcategory3daxis.cpp, line 128, as _ZN22QCategory3DAxisPrivate9allowZeroEv
inline bool QCategory3DAxisPrivate::allowZero()
{
    return true;
}

//  from ../qtdatavis3d/src/datavisualization/axis/qcategory3daxis.cpp, line 111, as _ZN22QCategory3DAxisPrivateD0Ev
inline QCategory3DAxisPrivate::~QCategory3DAxisPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/axis/qabstract3daxis.cpp, line 374, as _ZN22QAbstract3DAxisPrivateC2EP15QAbstract3DAxisNS0_8AxisTypeE
inline QAbstract3DAxisPrivate::QAbstract3DAxisPrivate(QAbstract3DAxis *q, QAbstract3DAxis::AxisType type)
    : QObject(0),
      q_ptr(q),
      m_orientation(QAbstract3DAxis::AxisOrientationNone),
      m_type(type),
      m_isDefaultAxis(false),
      m_min(0.0f),
      m_max(10.0f),
      m_autoAdjust(true),
      m_labelAutoRotation(0.0f),
      m_titleVisible(false),
      m_titleFixed(true)
{
}

//  from ../qtdatavis3d/src/datavisualization/axis/qabstract3daxis.cpp, line 389, as _ZN22QAbstract3DAxisPrivateD2Ev
inline QAbstract3DAxisPrivate::~QAbstract3DAxisPrivate()
{
}

//  from ../qtdatavis3d/src/datavisualization/axis/qcategory3daxis.cpp, line 105, as _ZN22QCategory3DAxisPrivateC1EP15QCategory3DAxis
inline QCategory3DAxisPrivate::QCategory3DAxisPrivate(QCategory3DAxis *q)
    : QAbstract3DAxisPrivate(q, QAbstract3DAxis::AxisTypeCategory),
      m_labelsExplicitlySet(false)
{
}

//  from ../qtdatavis3d/src/datavisualization/axis/qcategory3daxis.cpp, line 120, as _ZN22QCategory3DAxisPrivate13setDataLabelsERK5QListI7QStringE
inline void QCategory3DAxisPrivate::setDataLabels(const QStringList &labels)
{
    if (!m_labelsExplicitlySet && m_labels != labels) {
        m_labels = labels;
        emit qptr()->labelsChanged();
    }
}

//  from ../qtdatavis3d/src/datavisualization/axis/qcategory3daxis.cpp, line 143, as _ZN22QCategory3DAxisPrivate4qptrEv
inline QCategory3DAxis *QCategory3DAxisPrivate::qptr()
{
    return static_cast<QCategory3DAxis *>(q_ptr);
}
//  -----------------------------------------------------------------------

//  Only a class built on QCategory3DAxisPrivate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQCategory3DAxisPrivate : QCategory3DAxisPrivate {
  using QCategory3DAxisPrivate::allowZero;
  using QCategory3DAxisPrivate::allowNegatives;
  using QCategory3DAxisPrivate::allowMinMaxSame;
};

//  A QCategory3DAxisPrivate that Python can take functions over in. Every QCategory3DAxisPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQCategory3DAxisPrivateCall0)(const void *, int *);
typedef bool (*CuteQCategory3DAxisPrivateCall1)(const void *, int *);
typedef bool (*CuteQCategory3DAxisPrivateCall2)(const void *, int *);
typedef void (*CuteQCategory3DAxisPrivateCall3)(const void *, float, float, bool, int *);
typedef void (*CuteQCategory3DAxisPrivateCall4)(const void *, float, int *);
typedef void (*CuteQCategory3DAxisPrivateCall5)(const void *, float, int *);
typedef void (*CuteQCategory3DAxisPrivateCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCategory3DAxisPrivateCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCategory3DAxisPrivateCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCategory3DAxisPrivateCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCategory3DAxisPrivateCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCategory3DAxisPrivateCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCategory3DAxisPrivateCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCategory3DAxisPrivateCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCategory3DAxisPrivate : public QCategory3DAxisPrivate {
public:
  using QCategory3DAxisPrivate::QCategory3DAxisPrivate;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate9allowZeroEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate14allowNegativesEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate15allowMinMaxSameEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate8setRangeEffb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate6setMinEf")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate6setMaxEf")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstract3DAxisPrivate12updateLabelsEv")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QCategory3DAxisPrivate::allowZero()
  bool allowZero() override {
    if (taken[0]) {
      int handled = 0;
      CuteQCategory3DAxisPrivateCall0 call = reinterpret_cast<CuteQCategory3DAxisPrivateCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCategory3DAxisPrivate::allowZero();
  }

  //  bool QCategory3DAxisPrivate::allowNegatives()
  bool allowNegatives() override {
    if (taken[1]) {
      int handled = 0;
      CuteQCategory3DAxisPrivateCall1 call = reinterpret_cast<CuteQCategory3DAxisPrivateCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCategory3DAxisPrivate::allowNegatives();
  }

  //  bool QCategory3DAxisPrivate::allowMinMaxSame()
  bool allowMinMaxSame() override {
    if (taken[2]) {
      int handled = 0;
      CuteQCategory3DAxisPrivateCall2 call = reinterpret_cast<CuteQCategory3DAxisPrivateCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCategory3DAxisPrivate::allowMinMaxSame();
  }

  //  void QAbstract3DAxisPrivate::setRange(float min, float max, bool
  //      suppressWarnings)
  void setRange(float min, float max, bool suppressWarnings) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCategory3DAxisPrivateCall3 call = reinterpret_cast<CuteQCategory3DAxisPrivateCall3>(taken[3]);
      call(this, min, max, suppressWarnings, &handled);
      if (handled) return;
    }
    QAbstract3DAxisPrivate::setRange(min, max, suppressWarnings);
  }

  //  void QAbstract3DAxisPrivate::setMin(float min)
  void setMin(float min) override {
    if (taken[4]) {
      int handled = 0;
      CuteQCategory3DAxisPrivateCall4 call = reinterpret_cast<CuteQCategory3DAxisPrivateCall4>(taken[4]);
      call(this, min, &handled);
      if (handled) return;
    }
    QAbstract3DAxisPrivate::setMin(min);
  }

  //  void QAbstract3DAxisPrivate::setMax(float max)
  void setMax(float max) override {
    if (taken[5]) {
      int handled = 0;
      CuteQCategory3DAxisPrivateCall5 call = reinterpret_cast<CuteQCategory3DAxisPrivateCall5>(taken[5]);
      call(this, max, &handled);
      if (handled) return;
    }
    QAbstract3DAxisPrivate::setMax(max);
  }

  //  void QAbstract3DAxisPrivate::updateLabels()
  void updateLabels() override {
    if (taken[6]) {
      int handled = 0;
      CuteQCategory3DAxisPrivateCall6 call = reinterpret_cast<CuteQCategory3DAxisPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstract3DAxisPrivate::updateLabels();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQCategory3DAxisPrivateCall7 call = reinterpret_cast<CuteQCategory3DAxisPrivateCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQCategory3DAxisPrivateCall8 call = reinterpret_cast<CuteQCategory3DAxisPrivateCall8>(taken[8]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQCategory3DAxisPrivateCall9 call = reinterpret_cast<CuteQCategory3DAxisPrivateCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQCategory3DAxisPrivateCall10 call = reinterpret_cast<CuteQCategory3DAxisPrivateCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQCategory3DAxisPrivateCall11 call = reinterpret_cast<CuteQCategory3DAxisPrivateCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQCategory3DAxisPrivateCall12 call = reinterpret_cast<CuteQCategory3DAxisPrivateCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQCategory3DAxisPrivateCall13 call = reinterpret_cast<CuteQCategory3DAxisPrivateCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCategory3DAxisPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QCategory3DAxisPrivate10metaObjectEv(
    const QCategory3DAxisPrivate *self) {
  return self->metaObject();
}

//  void *QCategory3DAxisPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QCategory3DAxisPrivate11qt_metacastEPKc(
    QCategory3DAxisPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QCategory3DAxisPrivate::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QCategory3DAxisPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QCategory3DAxisPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QCategory3DAxisPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QCategory3DAxisPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCategory3DAxisPrivate::tr(s, c, n));
}

//  QCategory3DAxisPrivate::QCategory3DAxisPrivate(QCategory3DAxis *q)
extern "C" Q_DECL_EXPORT
QCategory3DAxisPrivate *ritual_ZN22QCategory3DAxisPrivateC1EP15QCategory3DAxis(
    QCategory3DAxis *q) {
  return new CuteQCategory3DAxisPrivate(q);
}

//  QCategory3DAxisPrivate::~QCategory3DAxisPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCategory3DAxisPrivateD1Ev(QCategory3DAxisPrivate *self) {
  delete self;
}

//  void QCategory3DAxisPrivate::setDataLabels(const QStringList &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCategory3DAxisPrivate13setDataLabelsERK5QListI7QStringE(
    QCategory3DAxisPrivate *self,
    const QList<QString> *labels) {
  self->setDataLabels(*labels);
}

//  bool QCategory3DAxisPrivate::allowZero()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QCategory3DAxisPrivate9allowZeroEv(
    QCategory3DAxisPrivate *self) {
  return self->allowZero();
}

//  bool QCategory3DAxisPrivate::allowNegatives()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QCategory3DAxisPrivate14allowNegativesEv(
    QCategory3DAxisPrivate *self) {
  return self->allowNegatives();
}

//  bool QCategory3DAxisPrivate::allowMinMaxSame()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QCategory3DAxisPrivate15allowMinMaxSameEv(
    QCategory3DAxisPrivate *self) {
  return self->allowMinMaxSame();
}

//  QCategory3DAxis *QCategory3DAxisPrivate::qptr()
extern "C" Q_DECL_EXPORT
QCategory3DAxis *ritual_ZN22QCategory3DAxisPrivate4qptrEv(
    QCategory3DAxisPrivate *self) {
  return self->qptr();
}

//  a Python function taken by a CuteQCategory3DAxisPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCategory3DAxisPrivate(
    QCategory3DAxisPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCategory3DAxisPrivate *>(self)->take(key, call);
}

//  bool QCategory3DAxisPrivate::allowZero()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QCategory3DAxisPrivate9allowZeroEv(
    QCategory3DAxisPrivate *self) {
  return static_cast<OwnQCategory3DAxisPrivate *>(self)->OwnQCategory3DAxisPrivate::allowZero();
}

//  bool QCategory3DAxisPrivate::allowNegatives()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QCategory3DAxisPrivate14allowNegativesEv(
    QCategory3DAxisPrivate *self) {
  return static_cast<OwnQCategory3DAxisPrivate *>(self)->OwnQCategory3DAxisPrivate::allowNegatives();
}

//  bool QCategory3DAxisPrivate::allowMinMaxSame()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QCategory3DAxisPrivate15allowMinMaxSameEv(
    QCategory3DAxisPrivate *self) {
  return static_cast<OwnQCategory3DAxisPrivate *>(self)->OwnQCategory3DAxisPrivate::allowMinMaxSame();
}
