//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtGui/qcolor.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/simplewidgets_p.h>
#if QT_CONFIG(abstractbutton)
#include <QtWidgets/qabstractbutton.h>
#endif
#if QT_CONFIG(checkbox)
#include <QtWidgets/qcheckbox.h>
#endif
#if QT_CONFIG(pushbutton)
#include <QtWidgets/qpushbutton.h>
#endif
#if QT_CONFIG(progressbar)
#include <QtWidgets/qprogressbar.h>
#endif
#if QT_CONFIG(statusbar)
#include <QtWidgets/qstatusbar.h>
#endif
#if QT_CONFIG(radiobutton)
#include <QtWidgets/qradiobutton.h>
#endif
#if QT_CONFIG(toolbutton)
#include <QtWidgets/qtoolbutton.h>
#endif
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#endif
#if QT_CONFIG(label)
#include <QtWidgets/qlabel.h>
#endif
#if QT_CONFIG(groupbox)
#include <QtWidgets/qgroupbox.h>
#endif
#if QT_CONFIG(lcdnumber)
#include <QtWidgets/qlcdnumber.h>
#endif
#if QT_CONFIG(lineedit)
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/private/qlineedit_p.h>
#endif
#ifndef QT_NO_PICTURE
#include <QtGui/qpicture.h>
#endif
#if QT_CONFIG(messagebox)
#include <QtWidgets/qmessagebox.h>
#endif
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qtextdocument.h>
#include <QtGui/qwindow.h>
#include <QtWidgets/private/qwindowcontainer_p.h>
#include <QtCore/qvarlengtharray.h>
#if QT_CONFIG(accessibility)
#include <QtGui/private/qaccessiblehelper_p.h>
#endif
#include <QtGui/qvalidator.h>
#ifdef Q_OS_MACOS
#include <QtWidgets/qfocusframe.h>
#endif
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

//  from src/widgets/accessible/simplewidgets.cpp, line 87, as _ZN17QAccessibleButtonC2EP7QWidget
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
inline QAccessibleButton::QAccessibleButton(QWidget *w)
: QAccessibleWidgetV2(w)
{
    Q_ASSERT(button());

    // FIXME: The checkable state of the button is dynamic,
    // while we only update the controlling signal once :(
    if (button()->isCheckable())
        addControllingSignal("toggled(bool)"_L1);
    else
        addControllingSignal("clicked()"_L1);
}
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 373, as _ZN21QAccessibleToolButton8doActionERK7QString
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
inline void QAccessibleToolButton::doAction(const QString &actionName)
{
    if (!widget()->isEnabled())
        return;

    if (actionName == pressAction()) {
        button()->click();
    } else if (actionName == showMenuAction()) {
#if QT_CONFIG(menu)
        if (toolButton()->popupMode() != QToolButton::InstantPopup) {
            toolButton()->setDown(true);
            toolButton()->showMenu();
        }
#endif
    } else {
        QAccessibleButton::doAction(actionName);
    }

}
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 252, as _ZNK17QAccessibleButton20keyBindingsForActionERK7QString
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
inline QStringList QAccessibleButton::keyBindingsForAction(const QString &actionName) const
{
    if (actionName == pressAction()) {
#ifndef QT_NO_SHORTCUT
        return QStringList() << button()->shortcut().toString();
#endif
    }
    return QStringList();
}
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 168, as _ZNK17QAccessibleButton4rectEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
inline QRect QAccessibleButton::rect() const
{
    QAbstractButton *ab = button();
    if (!ab->isVisible())
        return QRect();

#if QT_CONFIG(checkbox)
    if (QCheckBox *cb = qobject_cast<QCheckBox *>(ab)) {
        QPoint wpos = cb->mapToGlobal(QPoint(0, 0));
        QStyleOptionButton opt;
        cb->initStyleOption(&opt);
        return cb->style()->subElementRect(QStyle::SE_CheckBoxClickRect, &opt, cb).translated(wpos);
    }
#endif
#if QT_CONFIG(radiobutton)
    else if (QRadioButton *rb = qobject_cast<QRadioButton *>(ab)) {
        QPoint wpos = rb->mapToGlobal(QPoint(0, 0));
        QStyleOptionButton opt;
        rb->initStyleOption(&opt);
        return rb->style()->subElementRect(QStyle::SE_RadioButtonClickRect, &opt, rb).translated(wpos);
    }
#endif
    return QAccessibleWidgetV2::rect();
}
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 324, as _ZNK21QAccessibleToolButton10childCountEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
inline int QAccessibleToolButton::childCount() const
{
    return isSplitButton() ? 1 : 0;
}
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 359, as _ZNK21QAccessibleToolButton11actionNamesEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
inline QStringList QAccessibleToolButton::actionNames() const
{
    QStringList names;
    if (widget()->isEnabled()) {
#if QT_CONFIG(menu)
        if (toolButton()->menu())
            names << showMenuAction();
        if (toolButton()->popupMode() != QToolButton::InstantPopup)
            names << QAccessibleButton::actionNames();
#endif
    }
    return names;
}
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 329, as _ZNK21QAccessibleToolButton4roleEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
inline QAccessible::Role QAccessibleToolButton::role() const
{
#if QT_CONFIG(menu)
    QToolButton *tb = toolButton();
    if (!menu())
        return tb->isCheckable() ? QAccessible::CheckBox : QAccessible::PushButton;
    else if (tb->popupMode() == QToolButton::DelayedPopup)
        return QAccessible::ButtonDropDown;
#endif

    return QAccessible::ButtonMenu;
}
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 342, as _ZNK21QAccessibleToolButton5childEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
inline QAccessibleInterface *QAccessibleToolButton::child(int index) const
{
#if QT_CONFIG(menu)
    if (index == 0 && menu())
        return QAccessible::queryAccessibleInterface(menu());
#else
    Q_UNUSED(index);
#endif
    return nullptr;
}
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 312, as _ZNK21QAccessibleToolButton5stateEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
inline QAccessible::State QAccessibleToolButton::state() const
{
    QAccessible::State st = QAccessibleButton::state();
    if (toolButton()->autoRaise())
        st.hotTracked = true;
#if QT_CONFIG(menu)
    if (menu())
        st.hasPopup = true;
#endif
    return st;
}
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 135, as _ZNK17QAccessibleButton5stateEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
inline QAccessible::State QAccessibleButton::state() const
{
    QAccessible::State state = QAccessibleWidgetV2::state();

    QAbstractButton *b = button();
#if QT_CONFIG(checkbox)
    QCheckBox *cb = qobject_cast<QCheckBox *>(b);
#endif
    if (b->isCheckable())
        state.checkable = true;
    if (b->isChecked())
        state.checked = true;
#if QT_CONFIG(checkbox)
    if (cb && cb->checkState() == Qt::PartiallyChecked)
        state.checkStateMixed = true;
#endif
    if (b->isDown())
        state.pressed = true;
#if QT_CONFIG(pushbutton)
    QPushButton *pb = qobject_cast<QPushButton*>(b);
    if (pb) {
        if (pb->isDefault())
            state.defaultButton = true;
#if QT_CONFIG(menu)
        if (pb->menu())
            state.hasPopup = true;
#endif
    }
#endif

    return state;
}
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 232, as _ZN17QAccessibleButton8doActionERK7QString
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
inline void QAccessibleButton::doAction(const QString &actionName)
{
    if (!widget()->isEnabled())
        return;
    if (actionName == pressAction() ||
        actionName == showMenuAction()) {
#if QT_CONFIG(menu)
        QPushButton *pb = qobject_cast<QPushButton*>(object());
        if (pb && pb->menu())
            pb->showMenu();
        else
#endif
            button()->animateClick();
    } else if (actionName == toggleAction()) {
        button()->toggle();
    } else {
        QAccessibleWidgetV2::doAction(actionName);
    }
}
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 101, as _ZNK17QAccessibleButton6buttonEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
inline QAbstractButton *QAccessibleButton::button() const
{
    return qobject_cast<QAbstractButton*>(object());
}
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 282, as _ZNK21QAccessibleToolButton10toolButtonEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
inline QToolButton *QAccessibleToolButton::toolButton() const
{
    return qobject_cast<QToolButton*>(object());
}
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 290, as _ZNK21QAccessibleToolButton13isSplitButtonEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
inline bool QAccessibleToolButton::isSplitButton() const
{
#if QT_CONFIG(menu)
    return menu() && toolButton()->popupMode() == QToolButton::MenuButtonPopup;
#else
    return false;
#endif
}
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 300, as _ZNK21QAccessibleToolButton4menuEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(menu)
inline QMenu *QAccessibleToolButton::menu() const
{
    if (QMenu *menu = toolButton()->menu())
        return menu;

    if (QAction *defaultAction = toolButton()->defaultAction())
        return defaultAction->menu();

    return nullptr;
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleToolButton that Python can take functions over in. Every QAccessibleToolButton
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
typedef const QAccessible::State * (*CuteQAccessibleToolButtonCall0)(const void *, int *);
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
typedef int (*CuteQAccessibleToolButtonCall1)(const void *, int *);
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
typedef int (*CuteQAccessibleToolButtonCall2)(const void *, int *);
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
typedef void * (*CuteQAccessibleToolButtonCall3)(const void *, int, int *);
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
typedef void (*CuteQAccessibleToolButtonCall4)(const void *, const QString *, int *);
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
typedef QString * (*CuteQAccessibleToolButtonCall5)(const void *, int, int *);
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
typedef const QRect * (*CuteQAccessibleToolButtonCall6)(const void *, int *);
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleToolButtonCall7)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleToolButtonCall8)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleToolButtonCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleToolButtonCall10)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleToolButtonCall11)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleToolButtonCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleToolButtonCall13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleToolButtonCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleToolButtonCall15)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleToolButtonCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleToolButtonCall17)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleToolButtonCall18)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleToolButtonCall19)(const void *, int, void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleToolButtonCall20)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleToolButtonCall21)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleToolButton : public QAccessibleToolButton {
public:
  using QAccessibleToolButton::QAccessibleToolButton;
  void *taken[22] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface14interface_castEN11QAccessible13InterfaceTypeE")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface12virtual_hookEiPv")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
  //  QAccessible::State QAccessibleToolButton::state() const
  QAccessible::State state() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall0 call = reinterpret_cast<CuteQAccessibleToolButtonCall0>(taken[0]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleToolButton::state();
  }
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
  //  QAccessible::Role QAccessibleToolButton::role() const
  QAccessible::Role role() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall1 call = reinterpret_cast<CuteQAccessibleToolButtonCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleToolButton::role();
  }
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
  //  int QAccessibleToolButton::childCount() const
  int childCount() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall2 call = reinterpret_cast<CuteQAccessibleToolButtonCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleToolButton::childCount();
  }
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
  //  QAccessibleInterface *QAccessibleToolButton::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall3 call = reinterpret_cast<CuteQAccessibleToolButtonCall3>(taken[3]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleToolButton::child(index);
  }
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
  //  void QAccessibleToolButton::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall4 call = reinterpret_cast<CuteQAccessibleToolButtonCall4>(taken[4]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleToolButton::doAction(actionName);
  }
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
  //  QString QAccessibleButton::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall5 call = reinterpret_cast<CuteQAccessibleToolButtonCall5>(taken[5]);
      QString * given = call(this, static_cast<int>(t), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleButton::text(t);
  }
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
  //  QRect QAccessibleButton::rect() const
  QRect rect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall6 call = reinterpret_cast<CuteQAccessibleToolButtonCall6>(taken[6]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleButton::rect();
  }
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void *QAccessibleWidgetV2::interface_cast(QAccessible::InterfaceType
  //      t)
  void *interface_cast(QAccessible::InterfaceType t) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall7 call = reinterpret_cast<CuteQAccessibleToolButtonCall7>(taken[7]);
      void * given = call(this, static_cast<int>(t), &handled);
      if (handled) return static_cast<void *>(given);
    }
    return QAccessibleWidgetV2::interface_cast(t);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute
  //      key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall8 call = reinterpret_cast<CuteQAccessibleToolButtonCall8>(taken[8]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidgetV2::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleWidget::isValid() const
  bool isValid() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall9 call = reinterpret_cast<CuteQAccessibleToolButtonCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall10 call = reinterpret_cast<CuteQAccessibleToolButtonCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleWidget::indexOfChild(const QAccessibleInterface
  //      *child) const
  int indexOfChild(const QAccessibleInterface *child) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall11 call = reinterpret_cast<CuteQAccessibleToolButtonCall11>(taken[11]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::indexOfChild(child);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall12 call = reinterpret_cast<CuteQAccessibleToolButtonCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall13 call = reinterpret_cast<CuteQAccessibleToolButtonCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall14 call = reinterpret_cast<CuteQAccessibleToolButtonCall14>(taken[14]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall15 call = reinterpret_cast<CuteQAccessibleToolButtonCall15>(taken[15]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall16 call = reinterpret_cast<CuteQAccessibleToolButtonCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QAccessibleObject::object();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleObject::setText(QAccessible::Text t, const QString
  //      &text)
  void setText(QAccessible::Text t, const QString &text) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall17 call = reinterpret_cast<CuteQAccessibleToolButtonCall17>(taken[17]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall18 call = reinterpret_cast<CuteQAccessibleToolButtonCall18>(taken[18]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleObject::childAt(x, y);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleInterface::virtual_hook(int id, void *data)
  void virtual_hook(int id, void *data) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall19 call = reinterpret_cast<CuteQAccessibleToolButtonCall19>(taken[19]);
      call(this, id, data, &handled);
      if (handled) return;
    }
    QAccessibleInterface::virtual_hook(id, data);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleActionInterface::localizedActionName(const QString
  //      &name) const
  QString localizedActionName(const QString &name) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall20 call = reinterpret_cast<CuteQAccessibleToolButtonCall20>(taken[20]);
      QString * given = call(this, &name, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleActionInterface::localizedActionName(name);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleActionInterface::localizedActionDescription(const
  //      QString &name) const
  QString localizedActionDescription(const QString &name) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQAccessibleToolButtonCall21 call = reinterpret_cast<CuteQAccessibleToolButtonCall21>(taken[21]);
      QString * given = call(this, &name, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleActionInterface::localizedActionDescription(name);
  }
#endif  // QT_CONFIG(accessibility)
};

//  QAccessible::State QAccessibleToolButton::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK21QAccessibleToolButton5stateEv(
    const QAccessibleToolButton *self) {
  return new QAccessible::State(self->state());
}

//  QAccessible::Role QAccessibleToolButton::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK21QAccessibleToolButton4roleEv(
    const QAccessibleToolButton *self) {
  return self->role();
}

//  int QAccessibleToolButton::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAccessibleToolButton10childCountEv(
    const QAccessibleToolButton *self) {
  return self->childCount();
}

//  QAccessibleInterface *QAccessibleToolButton::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK21QAccessibleToolButton5childEi(
    const QAccessibleToolButton *self,
    int index) {
  return self->child(index);
}

//  QStringList QAccessibleToolButton::actionNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK21QAccessibleToolButton11actionNamesEv(
    const QAccessibleToolButton *self) {
  return new QList<QString>(self->actionNames());
}

//  void QAccessibleToolButton::doAction(const QString &actionName)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAccessibleToolButton8doActionERK7QString(
    QAccessibleToolButton *self,
    const QString *actionName) {
  self->doAction(*actionName);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
//  QToolButton *QAccessibleToolButton::toolButton() const
extern "C" Q_DECL_EXPORT
QToolButton *ritual_ZNK21QAccessibleToolButton10toolButtonEv(
    const QAccessibleToolButton *self) {
  return self->toolButton();
}
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(menu)
//  bool QAccessibleToolButton::isSplitButton() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QAccessibleToolButton13isSplitButtonEv(
    const QAccessibleToolButton *self) {
  return self->isSplitButton();
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(menu)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
//  QMenu *QAccessibleToolButton::menu() const
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZNK21QAccessibleToolButton4menuEv(
    const QAccessibleToolButton *self) {
  return self->menu();
}
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(menu)

//  a Python function taken by a CuteQAccessibleToolButton, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleToolButton(
    QAccessibleToolButton *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleToolButton *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(menu)
//  QAccessible::State QAccessibleToolButton::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_own_ZNK21QAccessibleToolButton5stateEv(
    const QAccessibleToolButton *self) {
  return new QAccessible::State(self->QAccessibleToolButton::state());
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(menu)
//  QAccessible::Role QAccessibleToolButton::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK21QAccessibleToolButton4roleEv(
    const QAccessibleToolButton *self) {
  return self->QAccessibleToolButton::role();
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(menu)
//  int QAccessibleToolButton::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QAccessibleToolButton10childCountEv(
    const QAccessibleToolButton *self) {
  return self->QAccessibleToolButton::childCount();
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(menu)
//  QAccessibleInterface *QAccessibleToolButton::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK21QAccessibleToolButton5childEi(
    const QAccessibleToolButton *self,
    int index) {
  return self->QAccessibleToolButton::child(index);
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
#if QT_CONFIG(toolbutton)
//  void QAccessibleToolButton::doAction(const QString &actionName)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QAccessibleToolButton8doActionERK7QString(
    QAccessibleToolButton *self,
    const QString *actionName) {
  self->QAccessibleToolButton::doAction(*actionName);
}
#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(toolbutton)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
