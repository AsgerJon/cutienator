//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qmdisubwindow_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(mdiarea)
#if QT_CONFIG(mdiarea)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qmdisubwindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qicon.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qmdisubwindow_p.h>
#include <QtWidgets/QApplication>
#include <QtWidgets/QStylePainter>
#include <QtWidgets/QVBoxLayout>
#include <QtGui/QMouseEvent>
#if QT_CONFIG(whatsthis)
#include <QtWidgets/QWhatsThis>
#endif
#if QT_CONFIG(tooltip)
#include <QtWidgets/QToolTip>
#endif
#if QT_CONFIG(mainwindow)
#include <QtWidgets/QMainWindow>
#endif
#include <QtWidgets/QScrollBar>
#include <QtCore/QDebug>
#include <QtWidgets/QMdiArea>
#include <QtCore/QScopedValueRollback>
#if QT_CONFIG(action)
#  include <QtWidgets/qaction.h>
#endif
#if QT_CONFIG(menu)
#include <QtWidgets/QMenu>
#endif
#include <QtWidgets/QProxyStyle>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/widgets/qmdisubwindow.cpp, line 362, as local:qmdisubwindow.cpp:ControlLabel
namespace QMdi {
using namespace Qt::StringLiterals;
using namespace std::chrono_literals;
class ControlLabel : public QWidget
{
    Q_OBJECT
public:
    ControlLabel(QWidget *parent = nullptr);

    QSize sizeHint() const override;

signals:
    void _q_clicked();
    void _q_doubleClicked();

protected:
    bool event(QEvent *event) override;
    void paintEvent(QPaintEvent *paintEvent) override;
    void mousePressEvent(QMouseEvent *mouseEvent) override;
    void mouseDoubleClickEvent(QMouseEvent *mouseEvent) override;
    void mouseReleaseEvent(QMouseEvent *mouseEvent) override;

private:
    QPixmap label;
    bool isPressed;
    void updateWindowIcon();
};
}  // namespace QMdi

//  from src/widgets/widgets/qmdisubwindow.cpp, line 493, as local:qmdisubwindow.cpp:ControllerWidget
namespace QMdi {
using namespace Qt::StringLiterals;
using namespace std::chrono_literals;
class ControllerWidget : public QWidget
{
    Q_OBJECT
public:
    ControllerWidget(QWidget *parent = nullptr);
    QSize sizeHint() const override;
    void setControlVisible(QMdiSubWindowPrivate::WindowStateAction action, bool visible);
    inline bool hasVisibleControls() const
    {
        return (visibleControls & QStyle::SC_MdiMinButton)
               || (visibleControls & QStyle::SC_MdiNormalButton)
               || (visibleControls & QStyle::SC_MdiCloseButton);
    }

signals:
    void _q_minimize();
    void _q_restore();
    void _q_close();

protected:
    void paintEvent(QPaintEvent *event) override;
    void mousePressEvent(QMouseEvent *event) override;
    void mouseReleaseEvent(QMouseEvent *event) override;
    void mouseMoveEvent(QMouseEvent *event) override;
    void leaveEvent(QEvent *event) override;
    bool event(QEvent *event) override;

private:
    QStyle::SubControl activeControl;
    QStyle::SubControl hoverControl;
    QStyle::SubControls visibleControls;
    void initStyleOption(QStyleOptionComplex *option) const;
    inline QStyle::SubControl getSubControl(const QPoint &pos) const
    {
        QStyleOptionComplex opt;
        initStyleOption(&opt);
        return style()->hitTestComplexControl(QStyle::CC_MdiControls, &opt, pos, this);
    }
};
}  // namespace QMdi

//  from src/widgets/widgets/qmdisubwindow.cpp, line 429, as _ZN4QMdi12ControlLabel10paintEventEP11QPaintEvent
namespace QMdi {
using namespace Qt::StringLiterals;
using namespace std::chrono_literals;
inline void ControlLabel::paintEvent(QPaintEvent * /*paintEvent*/)
{
    QPainter painter(this);
    painter.drawPixmap(0, 0, label);
}
}  // namespace QMdi

//  from src/widgets/widgets/qmdisubwindow.cpp, line 716, as _ZN4QMdi16ControlContainerD1Ev
namespace QMdi {
using namespace Qt::StringLiterals;
using namespace std::chrono_literals;
inline ControlContainer::~ControlContainer()
{
#if QT_CONFIG(menubar)
    removeButtonsFromMenuBar();
#endif
    delete m_menuLabel;
    m_menuLabel = nullptr;
    delete m_controllerWidget;
    m_controllerWidget = nullptr;
}
}  // namespace QMdi

//  from src/widgets/widgets/qmdisubwindow.cpp, line 841, as _ZN4QMdi16ControlContainer16updateWindowIconERK5QIcon
namespace QMdi {
using namespace Qt::StringLiterals;
using namespace std::chrono_literals;
inline void ControlContainer::updateWindowIcon(const QIcon &windowIcon)
{
    if (m_menuLabel)
        m_menuLabel->setWindowIcon(windowIcon);
}
}  // namespace QMdi
//  -----------------------------------------------------------------------

//  A QMdi::ControlContainer that Python can take functions over in. Every QMdi::ControlContainer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMdi_ControlContainerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMdi_ControlContainerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMdi_ControlContainerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMdi_ControlContainerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMdi_ControlContainerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMdi_ControlContainerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMdi_ControlContainerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQMdi_ControlContainer : public QMdi::ControlContainer {
public:
  using QMdi::ControlContainer::ControlContainer;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQMdi_ControlContainerCall0 call = reinterpret_cast<CuteQMdi_ControlContainerCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMdi_ControlContainerCall1 call = reinterpret_cast<CuteQMdi_ControlContainerCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMdi_ControlContainerCall2 call = reinterpret_cast<CuteQMdi_ControlContainerCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQMdi_ControlContainerCall3 call = reinterpret_cast<CuteQMdi_ControlContainerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMdi_ControlContainerCall4 call = reinterpret_cast<CuteQMdi_ControlContainerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQMdi_ControlContainerCall5 call = reinterpret_cast<CuteQMdi_ControlContainerCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQMdi_ControlContainerCall6 call = reinterpret_cast<CuteQMdi_ControlContainerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QMdi::ControlContainer::~ControlContainer()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QMdi16ControlContainerD1Ev(QMdi::ControlContainer *self) {
  delete self;
}

#if QT_CONFIG(menubar)
//  QMenuBar *QMdi::ControlContainer::menuBar() const
extern "C" Q_DECL_EXPORT
QMenuBar *ritual_ZNK4QMdi16ControlContainer7menuBarEv(
    const QMdi::ControlContainer *self) {
  return self->menuBar();
}
#endif  // QT_CONFIG(menubar)

//  void QMdi::ControlContainer::updateWindowIcon(const QIcon &windowIcon)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QMdi16ControlContainer16updateWindowIconERK5QIcon(
    QMdi::ControlContainer *self,
    const QIcon *windowIcon) {
  self->updateWindowIcon(*windowIcon);
}

//  QWidget *QMdi::ControlContainer::controllerWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK4QMdi16ControlContainer16controllerWidgetEv(
    const QMdi::ControlContainer *self) {
  return self->controllerWidget();
}

//  QWidget *QMdi::ControlContainer::systemMenuLabel() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK4QMdi16ControlContainer15systemMenuLabelEv(
    const QMdi::ControlContainer *self) {
  return self->systemMenuLabel();
}

//  a Python function taken by a CuteQMdi_ControlContainer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMdi_ControlContainer(
    QMdi::ControlContainer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMdi_ControlContainer *>(self)->take(key, call);
}

#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(mdiarea)
