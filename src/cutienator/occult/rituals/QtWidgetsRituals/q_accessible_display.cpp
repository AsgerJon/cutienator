//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qaccessible.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "simplewidgets_p.h"
#if QT_CONFIG(abstractbutton)
#include <qabstractbutton.h>
#endif
#if QT_CONFIG(checkbox)
#include <qcheckbox.h>
#endif
#if QT_CONFIG(pushbutton)
#include <qpushbutton.h>
#endif
#if QT_CONFIG(progressbar)
#include <qprogressbar.h>
#endif
#if QT_CONFIG(statusbar)
#include <qstatusbar.h>
#endif
#if QT_CONFIG(radiobutton)
#include <qradiobutton.h>
#endif
#if QT_CONFIG(toolbutton)
#include <qtoolbutton.h>
#endif
#if QT_CONFIG(menu)
#include <qmenu.h>
#endif
#if QT_CONFIG(label)
#include <qlabel.h>
#endif
#if QT_CONFIG(groupbox)
#include <qgroupbox.h>
#endif
#if QT_CONFIG(lcdnumber)
#include <qlcdnumber.h>
#endif
#if QT_CONFIG(lineedit)
#include <qlineedit.h>
#include <private/qlineedit_p.h>
#endif
#ifndef QT_NO_PICTURE
#include <QtGui/qpicture.h>
#endif
#if QT_CONFIG(messagebox)
#include <qmessagebox.h>
#endif
#include <qstyle.h>
#include <qstyleoption.h>
#include <qtextdocument.h>
#include <qwindow.h>
#include <private/qwindowcontainer_p.h>
#include <QtCore/qvarlengtharray.h>
#if QT_CONFIG(accessibility)
#include <QtGui/private/qaccessiblehelper_p.h>
#endif
#include <QtGui/qvalidator.h>
#ifdef Q_OS_MACOS
#include <qfocusframe.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/accessible/simplewidgets.cpp, line 519, as _ZN18QAccessibleDisplay14interface_castEN11QAccessible13InterfaceTypeE
#if QT_CONFIG(accessibility)
inline void *QAccessibleDisplay::interface_cast(QAccessible::InterfaceType t)
{
    if (t == QAccessible::ImageInterface)
        return static_cast<QAccessibleImageInterface*>(this);
    return QAccessibleWidgetV2::interface_cast(t);
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

//  from src/widgets/accessible/simplewidgets.cpp, line 407, as _ZN18QAccessibleDisplayC1EP7QWidgetN11QAccessible4RoleE
#if QT_CONFIG(accessibility)
inline QAccessibleDisplay::QAccessibleDisplay(QWidget *w, QAccessible::Role role)
: QAccessibleWidgetV2(w, role)
{
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

//  from src/widgets/accessible/simplewidgets.cpp, line 440, as _ZNK18QAccessibleDisplay5stateEv
#if QT_CONFIG(accessibility)
inline QAccessible::State QAccessibleDisplay::state() const
{
    QAccessible::State s = QAccessibleWidgetV2::state();
    s.readOnly = true;
    return s;
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
//  -----------------------------------------------------------------------

//  A QAccessibleDisplay that Python can take functions over in. Every QAccessibleDisplay
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleDisplayCall0)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleDisplayCall1)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleDisplayCall2)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleDisplayCall3)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QSize * (*CuteQAccessibleDisplayCall4)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QPoint * (*CuteQAccessibleDisplayCall5)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleDisplayCall6)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleDisplayCall7)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDisplayCall8)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleDisplayCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleDisplayCall10)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDisplayCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleDisplayCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDisplayCall13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDisplayCall14)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleDisplayCall15)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleDisplayCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleDisplayCall17)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDisplayCall18)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleDisplayCall19)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDisplayCall20)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleDisplayCall21)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleDisplayCall22)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleDisplay : public QAccessibleDisplay {
public:
  using QAccessibleDisplay::QAccessibleDisplay;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleImageInterface16imageDescriptionEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleImageInterface9imageSizeEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleImageInterface13imagePositionEv")) {
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
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
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
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
  //  QString QAccessibleDisplay::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleDisplayCall0 call = reinterpret_cast<CuteQAccessibleDisplayCall0>(taken[0]);
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
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleDisplayCall1 call = reinterpret_cast<CuteQAccessibleDisplayCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleDisplay::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::State QAccessibleDisplay::state() const
  QAccessible::State state() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleDisplayCall2 call = reinterpret_cast<CuteQAccessibleDisplayCall2>(taken[2]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleDisplay::state();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleDisplay::imageDescription() const
  QString imageDescription() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleDisplayCall3 call = reinterpret_cast<CuteQAccessibleDisplayCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleDisplayCall4 call = reinterpret_cast<CuteQAccessibleDisplayCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleDisplay::imageSize();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QPoint QAccessibleDisplay::imagePosition() const
  QPoint imagePosition() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleDisplayCall5 call = reinterpret_cast<CuteQAccessibleDisplayCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleDisplayCall6 call = reinterpret_cast<CuteQAccessibleDisplayCall6>(taken[6]);
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
      CuteQAccessibleDisplayCall7 call = reinterpret_cast<CuteQAccessibleDisplayCall7>(taken[7]);
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
      CuteQAccessibleDisplayCall8 call = reinterpret_cast<CuteQAccessibleDisplayCall8>(taken[8]);
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
      CuteQAccessibleDisplayCall9 call = reinterpret_cast<CuteQAccessibleDisplayCall9>(taken[9]);
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
      CuteQAccessibleDisplayCall10 call = reinterpret_cast<CuteQAccessibleDisplayCall10>(taken[10]);
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
      CuteQAccessibleDisplayCall11 call = reinterpret_cast<CuteQAccessibleDisplayCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleWidget::rect() const
  QRect rect() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleDisplayCall12 call = reinterpret_cast<CuteQAccessibleDisplayCall12>(taken[12]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleDisplayCall13 call = reinterpret_cast<CuteQAccessibleDisplayCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleDisplayCall14 call = reinterpret_cast<CuteQAccessibleDisplayCall14>(taken[14]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::child(index);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleDisplayCall15 call = reinterpret_cast<CuteQAccessibleDisplayCall15>(taken[15]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleDisplayCall16 call = reinterpret_cast<CuteQAccessibleDisplayCall16>(taken[16]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleWidget::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleDisplayCall17 call = reinterpret_cast<CuteQAccessibleDisplayCall17>(taken[17]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleWidget::doAction(actionName);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleDisplayCall18 call = reinterpret_cast<CuteQAccessibleDisplayCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleDisplayCall19 call = reinterpret_cast<CuteQAccessibleDisplayCall19>(taken[19]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQAccessibleDisplayCall20 call = reinterpret_cast<CuteQAccessibleDisplayCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQAccessibleDisplayCall21 call = reinterpret_cast<CuteQAccessibleDisplayCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQAccessibleDisplayCall22 call = reinterpret_cast<CuteQAccessibleDisplayCall22>(taken[22]);
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

#if QT_CONFIG(accessibility)
//  QAccessibleDisplay::QAccessibleDisplay(QWidget *w, QAccessible::Role
//      role)
extern "C" Q_DECL_EXPORT
QAccessibleDisplay *ritual_ZN18QAccessibleDisplayC1EP7QWidgetN11QAccessible4RoleE(
    QWidget *w,
    QAccessible::Role role) {
  return new CuteQAccessibleDisplay(w, role);
}
#endif  // QT_CONFIG(accessibility)

//  QString QAccessibleDisplay::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QAccessibleDisplay4textEN11QAccessible4TextE(
    const QAccessibleDisplay *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

//  QAccessible::Role QAccessibleDisplay::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK18QAccessibleDisplay4roleEv(
    const QAccessibleDisplay *self) {
  return self->role();
}

//  QAccessible::State QAccessibleDisplay::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK18QAccessibleDisplay5stateEv(
    const QAccessibleDisplay *self) {
  return new QAccessible::State(self->state());
}

//  QString QAccessibleDisplay::imageDescription() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QAccessibleDisplay16imageDescriptionEv(
    const QAccessibleDisplay *self) {
  return new QString(self->imageDescription());
}

//  QSize QAccessibleDisplay::imageSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18QAccessibleDisplay9imageSizeEv(
    const QAccessibleDisplay *self) {
  return new QSize(self->imageSize());
}

//  QPoint QAccessibleDisplay::imagePosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK18QAccessibleDisplay13imagePositionEv(
    const QAccessibleDisplay *self) {
  return new QPoint(self->imagePosition());
}

//  QAccessibleDisplay as the QAccessibleImageInterface it is built on
extern "C" Q_DECL_EXPORT
QAccessibleImageInterface *ritual_cast_QAccessibleDisplay_QAccessibleImageInterface(
    QAccessibleDisplay *self) {
  return static_cast<QAccessibleImageInterface *>(self);
}

//  a Python function taken by a CuteQAccessibleDisplay, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleDisplay(
    QAccessibleDisplay *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleDisplay *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
//  QString QAccessibleDisplay::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK18QAccessibleDisplay4textEN11QAccessible4TextE(
    const QAccessibleDisplay *self,
    QAccessible::Text t) {
  return new QString(self->QAccessibleDisplay::text(t));
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QAccessibleDisplay::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK18QAccessibleDisplay4roleEv(
    const QAccessibleDisplay *self) {
  return self->QAccessibleDisplay::role();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::State QAccessibleDisplay::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_own_ZNK18QAccessibleDisplay5stateEv(
    const QAccessibleDisplay *self) {
  return new QAccessible::State(self->QAccessibleDisplay::state());
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QString QAccessibleDisplay::imageDescription() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK18QAccessibleDisplay16imageDescriptionEv(
    const QAccessibleDisplay *self) {
  return new QString(self->QAccessibleDisplay::imageDescription());
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QSize QAccessibleDisplay::imageSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK18QAccessibleDisplay9imageSizeEv(
    const QAccessibleDisplay *self) {
  return new QSize(self->QAccessibleDisplay::imageSize());
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QPoint QAccessibleDisplay::imagePosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_own_ZNK18QAccessibleDisplay13imagePositionEv(
    const QAccessibleDisplay *self) {
  return new QPoint(self->QAccessibleDisplay::imagePosition());
}
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(accessibility)
