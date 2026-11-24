//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtoolbarlayout_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtoolbarlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qaction.h>
#include <QtWidgets/qwidgetaction.h>
#include <QtWidgets/qtoolbar.h>
#include <QtWidgets/qstyleoption.h>
#if QT_CONFIG(toolbutton)
#include <QtWidgets/qtoolbutton.h>
#endif
#include <QtWidgets/qmenu.h>
#include <QtCore/qdebug.h>
#include <QtCore/qmath.h>
#ifdef Q_OS_MACOS
#include <QtGui/qpa/qplatformnativeinterface.h>
#endif
#include <QtWidgets/private/qmainwindowlayout_p.h>
#if QT_CONFIG(toolbutton)
#include <QtWidgets/private/qtoolbarextension_p.h>
#endif
#include <QtWidgets/private/qtoolbarlayout_p.h>
#include <QtWidgets/private/qtoolbarseparator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 36, as _ZN12QToolBarItemC1EP7QWidget
inline QToolBarItem::QToolBarItem(QWidget *widget)
    : QWidgetItem(widget), action(nullptr), customWidget(false)
{
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 41, as _ZNK12QToolBarItem7isEmptyEv
inline bool QToolBarItem::isEmpty() const
{
    return action == nullptr || !action->isVisible();
}
//  -----------------------------------------------------------------------

//  A QToolBarItem that Python can take functions over in. Every QToolBarItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(toolbar)
typedef bool (*CuteQToolBarItemCall0)(const void *, int *);
#endif  // QT_CONFIG(toolbar)
typedef const QSize * (*CuteQToolBarItemCall1)(const void *, int *);
typedef const QSize * (*CuteQToolBarItemCall2)(const void *, int *);
typedef const QSize * (*CuteQToolBarItemCall3)(const void *, int *);
typedef int (*CuteQToolBarItemCall4)(const void *, int *);
typedef void (*CuteQToolBarItemCall5)(const void *, const QRect *, int *);
typedef const QRect * (*CuteQToolBarItemCall6)(const void *, int *);
typedef void * (*CuteQToolBarItemCall7)(const void *, int *);
typedef bool (*CuteQToolBarItemCall8)(const void *, int *);
typedef int (*CuteQToolBarItemCall9)(const void *, int, int *);
typedef int (*CuteQToolBarItemCall10)(const void *, int, int *);
typedef int (*CuteQToolBarItemCall11)(const void *, int *);
typedef void (*CuteQToolBarItemCall12)(const void *, int *);
typedef void * (*CuteQToolBarItemCall13)(const void *, int *);
typedef void * (*CuteQToolBarItemCall14)(const void *, int *);
class CuteQToolBarItem : public QToolBarItem {
public:
  using QToolBarItem::QToolBarItem;
  void *taken[15] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(toolbar)
    if (!std::strcmp(key, "_ZNK11QLayoutItem7isEmptyEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbar)
    if (!std::strcmp(key, "_ZNK11QLayoutItem8sizeHintEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem11minimumSizeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem11maximumSizeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem19expandingDirectionsEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem11setGeometryERK5QRect")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem8geometryEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem6widgetEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem17hasHeightForWidthEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem14heightForWidthEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem21minimumHeightForWidthEi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem12controlTypesEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem10invalidateEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem6layoutEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem10spacerItemEv")) {
      taken[14] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(toolbar)
  //  bool QToolBarItem::isEmpty() const
  bool isEmpty() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQToolBarItemCall0 call = reinterpret_cast<CuteQToolBarItemCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QToolBarItem::isEmpty();
  }
#endif  // QT_CONFIG(toolbar)

  //  QSize QWidgetItem::sizeHint() const
  QSize sizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQToolBarItemCall1 call = reinterpret_cast<CuteQToolBarItemCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetItem::sizeHint();
  }

  //  QSize QWidgetItem::minimumSize() const
  QSize minimumSize() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQToolBarItemCall2 call = reinterpret_cast<CuteQToolBarItemCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetItem::minimumSize();
  }

  //  QSize QWidgetItem::maximumSize() const
  QSize maximumSize() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQToolBarItemCall3 call = reinterpret_cast<CuteQToolBarItemCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetItem::maximumSize();
  }

  //  Qt::Orientations QWidgetItem::expandingDirections() const
  Qt::Orientations expandingDirections() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQToolBarItemCall4 call = reinterpret_cast<CuteQToolBarItemCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::Orientation>::fromInt(given);
    }
    return QWidgetItem::expandingDirections();
  }

  //  void QWidgetItem::setGeometry(const QRect &a0)
  void setGeometry(const QRect &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQToolBarItemCall5 call = reinterpret_cast<CuteQToolBarItemCall5>(taken[5]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QWidgetItem::setGeometry(a0);
  }

  //  QRect QWidgetItem::geometry() const
  QRect geometry() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQToolBarItemCall6 call = reinterpret_cast<CuteQToolBarItemCall6>(taken[6]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetItem::geometry();
  }

  //  QWidget *QWidgetItem::widget() const
  QWidget *widget() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQToolBarItemCall7 call = reinterpret_cast<CuteQToolBarItemCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QWidgetItem::widget();
  }

  //  bool QWidgetItem::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQToolBarItemCall8 call = reinterpret_cast<CuteQToolBarItemCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetItem::hasHeightForWidth();
  }

  //  int QWidgetItem::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQToolBarItemCall9 call = reinterpret_cast<CuteQToolBarItemCall9>(taken[9]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidgetItem::heightForWidth(a0);
  }

  //  int QWidgetItem::minimumHeightForWidth(int a0) const
  int minimumHeightForWidth(int a0) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQToolBarItemCall10 call = reinterpret_cast<CuteQToolBarItemCall10>(taken[10]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidgetItem::minimumHeightForWidth(a0);
  }

  //  QSizePolicy::ControlTypes QWidgetItem::controlTypes() const
  QSizePolicy::ControlTypes controlTypes() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQToolBarItemCall11 call = reinterpret_cast<CuteQToolBarItemCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSizePolicy::ControlType>::fromInt(given);
    }
    return QWidgetItem::controlTypes();
  }

  //  void QLayoutItem::invalidate()
  void invalidate() override {
    if (taken[12]) {
      int handled = 0;
      CuteQToolBarItemCall12 call = reinterpret_cast<CuteQToolBarItemCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QLayoutItem::invalidate();
  }

  //  QLayout *QLayoutItem::layout()
  QLayout *layout() override {
    if (taken[13]) {
      int handled = 0;
      CuteQToolBarItemCall13 call = reinterpret_cast<CuteQToolBarItemCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return QLayoutItem::layout();
  }

  //  QSpacerItem *QLayoutItem::spacerItem()
  QSpacerItem *spacerItem() override {
    if (taken[14]) {
      int handled = 0;
      CuteQToolBarItemCall14 call = reinterpret_cast<CuteQToolBarItemCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSpacerItem *>(given);
    }
    return QLayoutItem::spacerItem();
  }
};

//  QToolBarItem::QToolBarItem(QWidget *widget)
extern "C" Q_DECL_EXPORT
QToolBarItem *ritual_ZN12QToolBarItemC1EP7QWidget(QWidget *widget) {
  return new CuteQToolBarItem(widget);
}

//  bool QToolBarItem::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QToolBarItem7isEmptyEv(const QToolBarItem *self) {
  return self->isEmpty();
}

//  a Python function taken by a CuteQToolBarItem, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QToolBarItem(
    QToolBarItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQToolBarItem *>(self)->take(key, call);
}

//  bool QToolBarItem::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK12QToolBarItem7isEmptyEv(const QToolBarItem *self) {
  return self->QToolBarItem::isEmpty();
}

#endif  // QT_CONFIG(toolbar)
#endif  // QT_CONFIG(toolbar)
