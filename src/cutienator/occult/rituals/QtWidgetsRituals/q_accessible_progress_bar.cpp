//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtGui/qaccessible.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/accessible/simplewidgets.cpp, line 407, as _ZN18QAccessibleDisplayC2EP7QWidgetN11QAccessible4RoleE
#if QT_CONFIG(accessibility)
inline QAccessibleDisplay::QAccessibleDisplay(QWidget *w, QAccessible::Role role)
: QAccessibleWidgetV2(w, role)
{
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 884, as _ZN22QAccessibleProgressBar14interface_castEN11QAccessible13InterfaceTypeE
#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
inline void *QAccessibleProgressBar::interface_cast(QAccessible::InterfaceType t)
{
    if (t == QAccessible::ValueInterface)
        return static_cast<QAccessibleValueInterface*>(this);
    return QAccessibleDisplay::interface_cast(t);
}
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 550, as _ZNK18QAccessibleDisplay13imagePositionEv
#if QT_CONFIG(accessibility)
inline QPoint QAccessibleDisplay::imagePosition() const
{
#if QT_CONFIG(label)
    QLabel *label = qobject_cast<QLabel *>(widget());
    if (!label)
#endif
        return QPoint();
#if QT_CONFIG(label)
    if (label->pixmap().isNull())
        return QPoint();

    return QPoint(label->mapToGlobal(label->pos()));
#endif
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 527, as _ZNK18QAccessibleDisplay16imageDescriptionEv
#if QT_CONFIG(accessibility)
inline QString QAccessibleDisplay::imageDescription() const
{
#if QT_CONFIG(tooltip)
    return widget()->toolTip();
#else
    return QString();
#endif
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 412, as _ZNK18QAccessibleDisplay4roleEv
#if QT_CONFIG(accessibility)
inline QAccessible::Role QAccessibleDisplay::role() const
{
#if QT_CONFIG(label)
    QLabel *l = qobject_cast<QLabel*>(object());
    if (l) {
        if (!l->pixmap().isNull())
            return QAccessible::Graphic;
#ifndef QT_NO_PICTURE
        if (!l->picture().isNull())
            return QAccessible::Graphic;
#endif
#if QT_CONFIG(movie)
        if (l->movie())
            return QAccessible::Animation;
#endif
#if QT_CONFIG(progressbar)
    } else if (qobject_cast<QProgressBar*>(object())) {
        return QAccessible::ProgressBar;
#endif
#if QT_CONFIG(statusbar)
    } else if (qobject_cast<QStatusBar*>(object())) {
        return QAccessible::StatusBar;
#endif
    }
#endif
    return QAccessibleWidgetV2::role();
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 447, as _ZNK18QAccessibleDisplay4textEN11QAccessible4TextE
#if QT_CONFIG(accessibility)
inline QString QAccessibleDisplay::text(QAccessible::Text t) const
{
    QString str;
    switch (t) {
    case QAccessible::Name:
        str = widget()->accessibleName();
        if (str.isEmpty()) {
            if (false) {
#if QT_CONFIG(label)
            } else if (qobject_cast<QLabel*>(object())) {
                QLabel *label = qobject_cast<QLabel*>(object());
                str = label->text();
#ifndef QT_NO_TEXTHTMLPARSER
                if (label->textFormat() == Qt::RichText
                    || (label->textFormat() == Qt::AutoText && Qt::mightBeRichText(str))) {
                    QTextDocument doc;
                    doc.setHtml(str);
                    str = doc.toPlainText();
                }
#endif
#ifndef QT_NO_SHORTCUT
                if (label->buddy())
                    str = qt_accStripAmp(str);
#endif
#endif // QT_CONFIG(label)
#if QT_CONFIG(lcdnumber)
            } else if (qobject_cast<QLCDNumber*>(object())) {
                QLCDNumber *l = qobject_cast<QLCDNumber*>(object());
                if (l->digitCount())
                    str = QString::number(l->value());
                else
                    str = QString::number(l->intValue());
#endif
#if QT_CONFIG(statusbar)
            } else if (qobject_cast<QStatusBar*>(object())) {
                return qobject_cast<QStatusBar*>(object())->currentMessage();
#endif
            }
        }
        break;
    case QAccessible::Value:
#if QT_CONFIG(progressbar)
        if (qobject_cast<QProgressBar*>(object()))
            str = QString::number(qobject_cast<QProgressBar*>(object())->value());
#endif
        break;
    default:
        break;
    }
    if (str.isEmpty())
        str = QAccessibleWidgetV2::text(t);
    return str;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 440, as _ZNK18QAccessibleDisplay5stateEv
#if QT_CONFIG(accessibility)
inline QAccessible::State QAccessibleDisplay::state() const
{
    QAccessible::State s = QAccessibleWidgetV2::state();
    s.readOnly = true;
    return s;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 537, as _ZNK18QAccessibleDisplay9imageSizeEv
#if QT_CONFIG(accessibility)
inline QSize QAccessibleDisplay::imageSize() const
{
#if QT_CONFIG(label)
    QLabel *label = qobject_cast<QLabel *>(widget());
    if (!label)
#endif
        return QSize();
#if QT_CONFIG(label)
    return label->pixmap().size();
#endif
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 502, as _ZNK18QAccessibleDisplay9relationsE6QFlagsIN11QAccessible12RelationFlagEE
#if QT_CONFIG(accessibility)
inline QList<std::pair<QAccessibleInterface *, QAccessible::Relation>>
QAccessibleDisplay::relations(QAccessible::Relation match /* = QAccessible::AllRelations */) const
{
    QList<std::pair<QAccessibleInterface *, QAccessible::Relation>> rels =
            QAccessibleWidgetV2::relations(match);
#    if QT_CONFIG(shortcut) && QT_CONFIG(label)
    if (match & QAccessible::Labelled) {
        if (QLabel *label = qobject_cast<QLabel*>(object())) {
            const QAccessible::Relation rel = QAccessible::Labelled;
            if (QAccessibleInterface *iface = QAccessible::queryAccessibleInterface(label->buddy()))
                rels.emplace_back(iface, rel);
        }
    }
#endif
    return rels;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 891, as _ZNK22QAccessibleProgressBar12currentValueEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
inline QVariant QAccessibleProgressBar::currentValue() const
{
    return progressBar()->value();
}
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 896, as _ZNK22QAccessibleProgressBar12maximumValueEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
inline QVariant QAccessibleProgressBar::maximumValue() const
{
    return progressBar()->maximum();
}
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 901, as _ZNK22QAccessibleProgressBar12minimumValueEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
inline QVariant QAccessibleProgressBar::minimumValue() const
{
    return progressBar()->minimum();
}
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 906, as _ZNK22QAccessibleProgressBar15minimumStepSizeEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
inline QVariant QAccessibleProgressBar::minimumStepSize() const
{
    // This is arbitrary since any value between min and max is valid.
    // Some screen readers (orca use it to calculate how many digits to display though,
    // so it makes sense to return a "sensible" value. Providing 100 increments seems ok.
    return (progressBar()->maximum() - progressBar()->minimum()) / 100.0;
}
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 914, as _ZNK22QAccessibleProgressBar11progressBarEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
inline QProgressBar *QAccessibleProgressBar::progressBar() const
{
    return qobject_cast<QProgressBar *>(object());
}
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleProgressBar that Python can take functions over in. Every QAccessibleProgressBar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
typedef const QVariant * (*CuteQAccessibleProgressBarCall0)(const void *, int *);
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
typedef const QVariant * (*CuteQAccessibleProgressBarCall1)(const void *, int *);
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
typedef const QVariant * (*CuteQAccessibleProgressBarCall2)(const void *, int *);
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
typedef const QVariant * (*CuteQAccessibleProgressBarCall3)(const void *, int *);
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
typedef void (*CuteQAccessibleProgressBarCall4)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleProgressBarCall5)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleProgressBarCall6)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleProgressBarCall7)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleProgressBarCall8)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QSize * (*CuteQAccessibleProgressBarCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QPoint * (*CuteQAccessibleProgressBarCall10)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleProgressBarCall11)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleProgressBarCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleProgressBarCall13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleProgressBarCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleProgressBarCall15)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleProgressBarCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleProgressBarCall17)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleProgressBarCall18)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleProgressBarCall19)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleProgressBarCall20)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleProgressBarCall21)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleProgressBarCall22)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleProgressBarCall23)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleProgressBarCall24)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleProgressBarCall25)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleProgressBarCall26)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleProgressBarCall27)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleProgressBar : public QAccessibleProgressBar {
public:
  using QAccessibleProgressBar::QAccessibleProgressBar;
  void *taken[28] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12currentValueEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12maximumValueEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12minimumValueEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface15minimumStepSizeEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
    if (!std::strcmp(key, "_ZN25QAccessibleValueInterface15setCurrentValueERK8QVariant")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleImageInterface16imageDescriptionEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleImageInterface9imageSizeEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleImageInterface13imagePositionEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
  //  QVariant QAccessibleProgressBar::currentValue() const
  QVariant currentValue() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall0 call = reinterpret_cast<CuteQAccessibleProgressBarCall0>(taken[0]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleProgressBar::currentValue();
  }
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
  //  QVariant QAccessibleProgressBar::maximumValue() const
  QVariant maximumValue() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall1 call = reinterpret_cast<CuteQAccessibleProgressBarCall1>(taken[1]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleProgressBar::maximumValue();
  }
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
  //  QVariant QAccessibleProgressBar::minimumValue() const
  QVariant minimumValue() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall2 call = reinterpret_cast<CuteQAccessibleProgressBarCall2>(taken[2]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleProgressBar::minimumValue();
  }
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
  //  QVariant QAccessibleProgressBar::minimumStepSize() const
  QVariant minimumStepSize() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall3 call = reinterpret_cast<CuteQAccessibleProgressBarCall3>(taken[3]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleProgressBar::minimumStepSize();
  }
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
  //  void QAccessibleProgressBar::setCurrentValue(const QVariant &a0)
  void setCurrentValue(const QVariant &a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall4 call = reinterpret_cast<CuteQAccessibleProgressBarCall4>(taken[4]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QAccessibleProgressBar::setCurrentValue(a0);
  }
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleDisplay::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall5 call = reinterpret_cast<CuteQAccessibleProgressBarCall5>(taken[5]);
      QString * given = call(this, static_cast<int>(t), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleDisplay::text(t);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QAccessibleDisplay::role() const
  QAccessible::Role role() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall6 call = reinterpret_cast<CuteQAccessibleProgressBarCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleDisplay::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::State QAccessibleDisplay::state() const
  QAccessible::State state() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall7 call = reinterpret_cast<CuteQAccessibleProgressBarCall7>(taken[7]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleDisplay::state();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleDisplay::imageDescription() const
  QString imageDescription() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall8 call = reinterpret_cast<CuteQAccessibleProgressBarCall8>(taken[8]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleDisplay::imageDescription();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QSize QAccessibleDisplay::imageSize() const
  QSize imageSize() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall9 call = reinterpret_cast<CuteQAccessibleProgressBarCall9>(taken[9]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleDisplay::imageSize();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QPoint QAccessibleDisplay::imagePosition() const
  QPoint imagePosition() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall10 call = reinterpret_cast<CuteQAccessibleProgressBarCall10>(taken[10]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleDisplay::imagePosition();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute
  //      key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall11 call = reinterpret_cast<CuteQAccessibleProgressBarCall11>(taken[11]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidgetV2::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleWidget::isValid() const
  bool isValid() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall12 call = reinterpret_cast<CuteQAccessibleProgressBarCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall13 call = reinterpret_cast<CuteQAccessibleProgressBarCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleWidget::childCount() const
  int childCount() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall14 call = reinterpret_cast<CuteQAccessibleProgressBarCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall15 call = reinterpret_cast<CuteQAccessibleProgressBarCall15>(taken[15]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::indexOfChild(child);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall16 call = reinterpret_cast<CuteQAccessibleProgressBarCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleWidget::rect() const
  QRect rect() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall17 call = reinterpret_cast<CuteQAccessibleProgressBarCall17>(taken[17]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall18 call = reinterpret_cast<CuteQAccessibleProgressBarCall18>(taken[18]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall19 call = reinterpret_cast<CuteQAccessibleProgressBarCall19>(taken[19]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::child(index);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall20 call = reinterpret_cast<CuteQAccessibleProgressBarCall20>(taken[20]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall21 call = reinterpret_cast<CuteQAccessibleProgressBarCall21>(taken[21]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleWidget::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[22]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall22 call = reinterpret_cast<CuteQAccessibleProgressBarCall22>(taken[22]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleWidget::doAction(actionName);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall23 call = reinterpret_cast<CuteQAccessibleProgressBarCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall24 call = reinterpret_cast<CuteQAccessibleProgressBarCall24>(taken[24]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall25 call = reinterpret_cast<CuteQAccessibleProgressBarCall25>(taken[25]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleObject::childAt(x, y);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleActionInterface::localizedActionName(const QString
  //      &name) const
  QString localizedActionName(const QString &name) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall26 call = reinterpret_cast<CuteQAccessibleProgressBarCall26>(taken[26]);
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
    if (taken[27]) {
      int handled = 0;
      CuteQAccessibleProgressBarCall27 call = reinterpret_cast<CuteQAccessibleProgressBarCall27>(taken[27]);
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

//  QVariant QAccessibleProgressBar::currentValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QAccessibleProgressBar12currentValueEv(
    const QAccessibleProgressBar *self) {
  return new QVariant(self->currentValue());
}

//  QVariant QAccessibleProgressBar::maximumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QAccessibleProgressBar12maximumValueEv(
    const QAccessibleProgressBar *self) {
  return new QVariant(self->maximumValue());
}

//  QVariant QAccessibleProgressBar::minimumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QAccessibleProgressBar12minimumValueEv(
    const QAccessibleProgressBar *self) {
  return new QVariant(self->minimumValue());
}

//  QVariant QAccessibleProgressBar::minimumStepSize() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QAccessibleProgressBar15minimumStepSizeEv(
    const QAccessibleProgressBar *self) {
  return new QVariant(self->minimumStepSize());
}

//  void QAccessibleProgressBar::setCurrentValue(const QVariant &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAccessibleProgressBar15setCurrentValueERK8QVariant(
    QAccessibleProgressBar *self,
    const QVariant *a0) {
  self->setCurrentValue(*a0);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
//  QProgressBar *QAccessibleProgressBar::progressBar() const
extern "C" Q_DECL_EXPORT
QProgressBar *ritual_ZNK22QAccessibleProgressBar11progressBarEv(
    const QAccessibleProgressBar *self) {
  return self->progressBar();
}
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)

//  QAccessibleProgressBar as the QAccessibleValueInterface it is built on
extern "C" Q_DECL_EXPORT
QAccessibleValueInterface *ritual_cast_QAccessibleProgressBar_QAccessibleValueInterface(
    QAccessibleProgressBar *self) {
  return static_cast<QAccessibleValueInterface *>(self);
}

//  a Python function taken by a CuteQAccessibleProgressBar, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleProgressBar(
    QAccessibleProgressBar *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleProgressBar *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
//  QVariant QAccessibleProgressBar::currentValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK22QAccessibleProgressBar12currentValueEv(
    const QAccessibleProgressBar *self) {
  return new QVariant(self->QAccessibleProgressBar::currentValue());
}
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
//  QVariant QAccessibleProgressBar::maximumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK22QAccessibleProgressBar12maximumValueEv(
    const QAccessibleProgressBar *self) {
  return new QVariant(self->QAccessibleProgressBar::maximumValue());
}
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
//  QVariant QAccessibleProgressBar::minimumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK22QAccessibleProgressBar12minimumValueEv(
    const QAccessibleProgressBar *self) {
  return new QVariant(self->QAccessibleProgressBar::minimumValue());
}
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(progressbar)
//  QVariant QAccessibleProgressBar::minimumStepSize() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK22QAccessibleProgressBar15minimumStepSizeEv(
    const QAccessibleProgressBar *self) {
  return new QVariant(self->QAccessibleProgressBar::minimumStepSize());
}
#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)

//  void QAccessibleProgressBar::setCurrentValue(const QVariant &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QAccessibleProgressBar15setCurrentValueERK8QVariant(
    QAccessibleProgressBar *self,
    const QVariant *a0) {
  self->QAccessibleProgressBar::setCurrentValue(*a0);
}

#endif  // QT_CONFIG(progressbar)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
