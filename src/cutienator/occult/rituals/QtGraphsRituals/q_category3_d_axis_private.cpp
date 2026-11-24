//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qcategory3daxis_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if !(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qcategory3daxis.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qcategory3daxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/private/qcategory3daxis_p.h>
#include <QtGraphs/private/qquickgraphsitem_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs3d/axis/qcategory3daxis.cpp, line 144, as _ZN22QCategory3DAxisPrivate9allowZeroEv
inline bool QCategory3DAxisPrivate::allowZero()
{
    return true;
}

//  from ../qtgraphs/src/graphs3d/axis/qcategory3daxis.cpp, line 149, as _ZN22QCategory3DAxisPrivate14allowNegativesEv
inline bool QCategory3DAxisPrivate::allowNegatives()
{
    return false;
}

//  from ../qtgraphs/src/graphs3d/axis/qcategory3daxis.cpp, line 154, as _ZN22QCategory3DAxisPrivate15allowMinMaxSameEv
inline bool QCategory3DAxisPrivate::allowMinMaxSame()
{
    return true;
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
class CuteQCategory3DAxisPrivate : public QCategory3DAxisPrivate {
public:
  using QCategory3DAxisPrivate::QCategory3DAxisPrivate;
  void *taken[7] = {};

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
};

//  QCategory3DAxis *QCategory3DAxisPrivate::q_func()
extern "C" Q_DECL_EXPORT
QCategory3DAxis *ritual_ZN22QCategory3DAxisPrivate6q_funcEv(
    QCategory3DAxisPrivate *self) {
  return self->q_func();
}

//  const QCategory3DAxis *QCategory3DAxisPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QCategory3DAxis *ritual_ZNK22QCategory3DAxisPrivate6q_funcEv(
    const QCategory3DAxisPrivate *self) {
  return self->q_func();
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

#endif  // !(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))
