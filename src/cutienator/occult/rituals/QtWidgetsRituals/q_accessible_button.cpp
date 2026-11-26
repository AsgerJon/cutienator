//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qaccessible.h>
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

//  from src/widgets/accessible/simplewidgets.cpp, line 210, as _ZNK17QAccessibleButton11actionNamesEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
inline QStringList QAccessibleButton::actionNames() const
{
    QStringList names;
    if (widget()->isEnabled()) {
        switch (role()) {
        case QAccessible::ButtonMenu:
            names << showMenuAction();
            break;
        case QAccessible::RadioButton:
            names << toggleAction();
            break;
        default:
            if (button()->isCheckable())
                names <<  toggleAction();
            names << pressAction();
            break;
        }
    }
    names << QAccessibleWidgetV2::actionNames();
    return names;
}
#endif  // QT_CONFIG(abstractbutton)
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

//  from src/widgets/accessible/simplewidgets.cpp, line 193, as _ZNK17QAccessibleButton4roleEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
inline QAccessible::Role QAccessibleButton::role() const
{
    QAbstractButton *ab = button();

#if QT_CONFIG(menu)
    if (QPushButton *pb = qobject_cast<QPushButton*>(ab)) {
        if (pb->menu())
            return QAccessible::ButtonMenu;
    }
#endif

    if (ab->isCheckable())
        return ab->autoExclusive() ? QAccessible::RadioButton : QAccessible::CheckBox;

    return QAccessible::Button;
}
#endif  // QT_CONFIG(abstractbutton)
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

//  from src/widgets/accessible/simplewidgets.cpp, line 101, as _ZNK17QAccessibleButton6buttonEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
inline QAbstractButton *QAccessibleButton::button() const
{
    return qobject_cast<QAbstractButton*>(object());
}
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleButton that Python can take functions over in. Every QAccessibleButton
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
typedef QString * (*CuteQAccessibleButtonCall0)(const void *, int, int *);
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
typedef const QAccessible::State * (*CuteQAccessibleButtonCall1)(const void *, int *);
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
typedef const QRect * (*CuteQAccessibleButtonCall2)(const void *, int *);
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
typedef int (*CuteQAccessibleButtonCall3)(const void *, int *);
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
typedef void (*CuteQAccessibleButtonCall4)(const void *, const QString *, int *);
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleButtonCall5)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleButtonCall6)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleButtonCall7)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleButtonCall8)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleButtonCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleButtonCall10)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleButtonCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleButtonCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleButtonCall13)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleButtonCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleButtonCall15)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleButtonCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleButtonCall17)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleButtonCall18)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleButtonCall19)(const void *, int, void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleButtonCall20)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleButtonCall21)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleButton : public QAccessibleButton {
public:
  using QAccessibleButton::QAccessibleButton;
  void *taken[22] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface14interface_castEN11QAccessible13InterfaceTypeE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
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
#if QT_CONFIG(abstractbutton)
  //  QString QAccessibleButton::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleButtonCall0 call = reinterpret_cast<CuteQAccessibleButtonCall0>(taken[0]);
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
  //  QAccessible::State QAccessibleButton::state() const
  QAccessible::State state() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleButtonCall1 call = reinterpret_cast<CuteQAccessibleButtonCall1>(taken[1]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleButton::state();
  }
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
  //  QRect QAccessibleButton::rect() const
  QRect rect() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleButtonCall2 call = reinterpret_cast<CuteQAccessibleButtonCall2>(taken[2]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleButton::rect();
  }
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
  //  QAccessible::Role QAccessibleButton::role() const
  QAccessible::Role role() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleButtonCall3 call = reinterpret_cast<CuteQAccessibleButtonCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleButton::role();
  }
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
  //  void QAccessibleButton::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleButtonCall4 call = reinterpret_cast<CuteQAccessibleButtonCall4>(taken[4]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleButton::doAction(actionName);
  }
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void *QAccessibleWidgetV2::interface_cast(QAccessible::InterfaceType
  //      t)
  void *interface_cast(QAccessible::InterfaceType t) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleButtonCall5 call = reinterpret_cast<CuteQAccessibleButtonCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleButtonCall6 call = reinterpret_cast<CuteQAccessibleButtonCall6>(taken[6]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidgetV2::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleWidget::isValid() const
  bool isValid() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleButtonCall7 call = reinterpret_cast<CuteQAccessibleButtonCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleButtonCall8 call = reinterpret_cast<CuteQAccessibleButtonCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleWidget::childCount() const
  int childCount() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleButtonCall9 call = reinterpret_cast<CuteQAccessibleButtonCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::childCount();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleWidget::indexOfChild(const QAccessibleInterface
  //      *child) const
  int indexOfChild(const QAccessibleInterface *child) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleButtonCall10 call = reinterpret_cast<CuteQAccessibleButtonCall10>(taken[10]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::indexOfChild(child);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleButtonCall11 call = reinterpret_cast<CuteQAccessibleButtonCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleButtonCall12 call = reinterpret_cast<CuteQAccessibleButtonCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleButtonCall13 call = reinterpret_cast<CuteQAccessibleButtonCall13>(taken[13]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::child(index);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleButtonCall14 call = reinterpret_cast<CuteQAccessibleButtonCall14>(taken[14]);
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
      CuteQAccessibleButtonCall15 call = reinterpret_cast<CuteQAccessibleButtonCall15>(taken[15]);
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
      CuteQAccessibleButtonCall16 call = reinterpret_cast<CuteQAccessibleButtonCall16>(taken[16]);
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
      CuteQAccessibleButtonCall17 call = reinterpret_cast<CuteQAccessibleButtonCall17>(taken[17]);
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
      CuteQAccessibleButtonCall18 call = reinterpret_cast<CuteQAccessibleButtonCall18>(taken[18]);
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
      CuteQAccessibleButtonCall19 call = reinterpret_cast<CuteQAccessibleButtonCall19>(taken[19]);
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
      CuteQAccessibleButtonCall20 call = reinterpret_cast<CuteQAccessibleButtonCall20>(taken[20]);
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
      CuteQAccessibleButtonCall21 call = reinterpret_cast<CuteQAccessibleButtonCall21>(taken[21]);
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

//  QString QAccessibleButton::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QAccessibleButton2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(QAccessibleButton::tr(sourceText, disambiguation, n));
}

//  QString QAccessibleButton::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QAccessibleButton4textEN11QAccessible4TextE(
    const QAccessibleButton *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

//  QAccessible::State QAccessibleButton::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK17QAccessibleButton5stateEv(
    const QAccessibleButton *self) {
  return new QAccessible::State(self->state());
}

//  QRect QAccessibleButton::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK17QAccessibleButton4rectEv(const QAccessibleButton *self) {
  return new QRect(self->rect());
}

//  QAccessible::Role QAccessibleButton::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK17QAccessibleButton4roleEv(
    const QAccessibleButton *self) {
  return self->role();
}

//  QStringList QAccessibleButton::actionNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QAccessibleButton11actionNamesEv(
    const QAccessibleButton *self) {
  return new QList<QString>(self->actionNames());
}

//  void QAccessibleButton::doAction(const QString &actionName)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAccessibleButton8doActionERK7QString(
    QAccessibleButton *self,
    const QString *actionName) {
  self->doAction(*actionName);
}

//  QStringList QAccessibleButton::keyBindingsForAction(const QString
//      &actionName) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QAccessibleButton20keyBindingsForActionERK7QString(
    const QAccessibleButton *self,
    const QString *actionName) {
  return new QList<QString>(self->keyBindingsForAction(*actionName));
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
//  QAbstractButton *QAccessibleButton::button() const
extern "C" Q_DECL_EXPORT
QAbstractButton *ritual_ZNK17QAccessibleButton6buttonEv(
    const QAccessibleButton *self) {
  return self->button();
}
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)

//  a Python function taken by a CuteQAccessibleButton, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleButton(
    QAccessibleButton *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleButton *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
//  QAccessible::State QAccessibleButton::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_own_ZNK17QAccessibleButton5stateEv(
    const QAccessibleButton *self) {
  return new QAccessible::State(self->QAccessibleButton::state());
}
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
//  QRect QAccessibleButton::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK17QAccessibleButton4rectEv(
    const QAccessibleButton *self) {
  return new QRect(self->QAccessibleButton::rect());
}
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
//  QAccessible::Role QAccessibleButton::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK17QAccessibleButton4roleEv(
    const QAccessibleButton *self) {
  return self->QAccessibleButton::role();
}
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(abstractbutton)
//  void QAccessibleButton::doAction(const QString &actionName)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAccessibleButton8doActionERK7QString(
    QAccessibleButton *self,
    const QString *actionName) {
  self->QAccessibleButton::doAction(*actionName);
}
#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(abstractbutton)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
