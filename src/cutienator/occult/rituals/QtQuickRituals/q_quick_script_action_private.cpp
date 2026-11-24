//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 1003, as _ZN25QQuickScriptActionPrivate7executeEv
inline void QQuickScriptActionPrivate::execute()
{
    Q_Q(QQuickScriptAction);
    if (hasRunScriptScript && reversing)
        return;

    QQmlScriptString scriptStr = hasRunScriptScript ? runScriptScript : script;

    if (!scriptStr.isEmpty()) {
        QQmlExpression expr(scriptStr);
        expr.evaluate();
        if (expr.hasError())
            qmlWarning(q) << expr.error();
    }
}

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 982, as _ZN25QQuickScriptActionPrivate12createActionEv
inline QAbstractAnimationAction* QQuickScriptActionPrivate::createAction()
{
    return new Proxy(this);
}

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 987, as _ZNK25QQuickScriptActionPrivate11debugActionE6QDebugi
inline void QQuickScriptActionPrivate::debugAction(QDebug d, int indentLevel) const
{
    QQmlScriptString scriptStr = hasRunScriptScript ? runScriptScript : script;

    if (!scriptStr.isEmpty()) {
        QQmlExpression expr(scriptStr);

        QByteArray ind(indentLevel, u' ');
        QString exprStr = expr.expression();
        int endOfFirstLine = exprStr.indexOf(u'\n');
        d << "\n" << ind.constData() << QStringView{exprStr}.left(endOfFirstLine);
        if (endOfFirstLine != -1 && endOfFirstLine < exprStr.size())
            d << "...";
    }
}
//  -----------------------------------------------------------------------

//  A QQuickScriptActionPrivate that Python can take functions over in. Every QQuickScriptActionPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickScriptActionPrivateCall0)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickScriptActionPrivateCall1)(const void *, QAbstractAnimationJob *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickScriptActionPrivateCall2)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickScriptActionPrivateCall3)(const void *, QAbstractAnimationJob *, int, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQQuickScriptActionPrivate : public QQuickScriptActionPrivate {
public:
  using QQuickScriptActionPrivate::QQuickScriptActionPrivate;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener17animationFinishedEP21QAbstractAnimationJob")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener21animationStateChangedEP21QAbstractAnimationJobNS0_5StateES2_")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener27animationCurrentLoopChangedEP21QAbstractAnimationJob")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener27animationCurrentTimeChangedEP21QAbstractAnimationJobi")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
    return false;
  }

#if QT_CONFIG(qml_animation)
  //  void QQuickAbstractAnimationPrivate::animationFinished(QAbstractAnima
  //      tionJob *a0)
  void animationFinished(QAbstractAnimationJob *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickScriptActionPrivateCall0 call = reinterpret_cast<CuteQQuickScriptActionPrivateCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimationPrivate::animationFinished(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationJobChangeListener::animationStateChanged(QAbstractAnim
  //      ationJob *a0, QAbstractAnimationJob::State a1,
  //      QAbstractAnimationJob::State a2)
  void animationStateChanged(
      QAbstractAnimationJob *a0,
      QAbstractAnimationJob::State a1,
      QAbstractAnimationJob::State a2) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickScriptActionPrivateCall1 call = reinterpret_cast<CuteQQuickScriptActionPrivateCall1>(taken[1]);
      call(this, a0, static_cast<int>(a1), static_cast<int>(a2), &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationStateChanged(a0, a1, a2);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationJobChangeListener::animationCurrentLoopChanged(QAbstra
  //      ctAnimationJob *a0)
  void animationCurrentLoopChanged(QAbstractAnimationJob *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickScriptActionPrivateCall2 call = reinterpret_cast<CuteQQuickScriptActionPrivateCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationCurrentLoopChanged(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationJobChangeListener::animationCurrentTimeChanged(QAbstra
  //      ctAnimationJob *a0, int a1)
  void animationCurrentTimeChanged(
      QAbstractAnimationJob *a0,
      int a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickScriptActionPrivateCall3 call = reinterpret_cast<CuteQQuickScriptActionPrivateCall3>(taken[3]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationCurrentTimeChanged(a0, a1);
  }
#endif  // QT_CONFIG(qml_animation)
};

//  QQuickScriptAction *QQuickScriptActionPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickScriptAction *ritual_ZN25QQuickScriptActionPrivate6q_funcEv(
    QQuickScriptActionPrivate *self) {
  return self->q_func();
}

//  const QQuickScriptAction *QQuickScriptActionPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickScriptAction *ritual_ZNK25QQuickScriptActionPrivate6q_funcEv(
    const QQuickScriptActionPrivate *self) {
  return self->q_func();
}

//  void QQuickScriptActionPrivate::execute()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickScriptActionPrivate7executeEv(
    QQuickScriptActionPrivate *self) {
  self->execute();
}

//  QAbstractAnimationAction *QQuickScriptActionPrivate::createAction()
extern "C" Q_DECL_EXPORT
QAbstractAnimationAction *ritual_ZN25QQuickScriptActionPrivate12createActionEv(
    QQuickScriptActionPrivate *self) {
  return self->createAction();
}

//  void QQuickScriptActionPrivate::debugAction(QDebug d, int indentLevel)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK25QQuickScriptActionPrivate11debugActionE6QDebugi(
    const QQuickScriptActionPrivate *self,
    const QDebug *d,
    int indentLevel) {
  self->debugAction(*d, indentLevel);
}

//  a Python function taken by a CuteQQuickScriptActionPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickScriptActionPrivate(
    QQuickScriptActionPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickScriptActionPrivate *>(self)->take(key, call);
}
