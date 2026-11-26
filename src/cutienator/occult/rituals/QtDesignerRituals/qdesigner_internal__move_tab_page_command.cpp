//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qicon.h>
#include <QtCore/qstring.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/private/qdesigner_command_p.h>
#include <QtDesigner/private/qdesigner_utils_p.h>
#include <QtDesigner/private/layout_p.h>
#include <QtDesigner/private/qlayout_widget_p.h>
#include <QtDesigner/private/qdesigner_widget_p.h>
#include <QtDesigner/private/qdesigner_menu_p.h>
#include <QtDesigner/private/shared_enums_p.h>
#include <QtDesigner/private/metadatabase_p.h>
#include <QtDesigner/private/formwindowbase_p.h>
#include <QtDesigner/abstractformbuilder.h>
#include <QtDesigner/abstractformwindow.h>
#include <QtDesigner/abstractformeditor.h>
#include <QtDesigner/propertysheet.h>
#include <QtDesigner/abstractactioneditor.h>
#include <QtDesigner/abstractpropertyeditor.h>
#include <QtDesigner/qextensionmanager.h>
#include <QtDesigner/container.h>
#include <QtDesigner/layoutdecoration.h>
#include <QtDesigner/abstractwidgetfactory.h>
#include <QtDesigner/abstractobjectinspector.h>
#include <QtDesigner/abstractintegration.h>
#include <QtDesigner/abstractformwindowcursor.h>
#include <QtCore/qdebug.h>
#include <QtCore/qtextstream.h>
#include <QtCore/qqueue.h>
#include <QtWidgets/qmenubar.h>
#include <QtWidgets/qstatusbar.h>
#include <QtWidgets/qtoolbar.h>
#include <QtWidgets/qtoolbox.h>
#include <QtWidgets/qstackedwidget.h>
#include <QtWidgets/qtabwidget.h>
#include <QtWidgets/qtablewidget.h>
#include <QtWidgets/qtreewidget.h>
#include <QtWidgets/qlistwidget.h>
#include <QtWidgets/qcombobox.h>
#include <QtWidgets/qsplitter.h>
#include <QtWidgets/qdockwidget.h>
#include <QtWidgets/qmainwindow.h>
#include <QtWidgets/qwizard.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qformlayout.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1078, as _ZN18qdesigner_internal16TabWidgetCommandC2EP28QDesignerFormWindowInterface
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline TabWidgetCommand::TabWidgetCommand(QDesignerFormWindowInterface *formWindow) :
    QDesignerFormWindowCommand(QString(), formWindow),
    m_index(-1)
{
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1219, as _ZN18qdesigner_internal18MoveTabPageCommand4redoEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void MoveTabPageCommand::redo()
{
    m_tabWidget->removeTab(m_oldIndex);
    m_tabWidget->insertTab(m_newIndex, m_page, m_icon, m_label);
    m_tabWidget->setCurrentIndex(m_newIndex);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1226, as _ZN18qdesigner_internal18MoveTabPageCommand4undoEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void MoveTabPageCommand::undo()
{
    m_tabWidget->removeTab(m_newIndex);
    m_tabWidget->insertTab(m_oldIndex, m_page, m_icon, m_label);
    m_tabWidget->setCurrentIndex(m_oldIndex);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1203, as _ZN18qdesigner_internal18MoveTabPageCommandD2Ev
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline MoveTabPageCommand::~MoveTabPageCommand() = default;
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1086, as _ZN18qdesigner_internal16TabWidgetCommand4initEP10QTabWidget
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void TabWidgetCommand::init(QTabWidget *tabWidget)
{
    m_tabWidget = tabWidget;
    m_index = m_tabWidget->currentIndex();
    m_widget = m_tabWidget->widget(m_index);
    m_itemText = m_tabWidget->tabText(m_index);
    m_itemIcon = m_tabWidget->tabIcon(m_index);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 1205, as _ZN18qdesigner_internal18MoveTabPageCommand4initEP10QTabWidgetP7QWidgetRK5QIconRK7QStringii
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void MoveTabPageCommand::init(QTabWidget *tabWidget, QWidget *page,
                      const QIcon &icon, const QString &label,
                      int index, int newIndex)
{
    TabWidgetCommand::init(tabWidget);
    setText(QApplication::translate("Command", "Move Page"));

    m_page = page;
    m_newIndex = newIndex;
    m_oldIndex = index;
    m_label = label;
    m_icon = icon;
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  A qdesigner_internal::MoveTabPageCommand that Python can take functions over in. Every qdesigner_internal::MoveTabPageCommand
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_MoveTabPageCommandCall0)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_MoveTabPageCommandCall1)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef int (*Cuteqdesigner_internal_MoveTabPageCommandCall2)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef bool (*Cuteqdesigner_internal_MoveTabPageCommandCall3)(const void *, const QUndoCommand *, int *);
#endif  // QT_CONFIG(undocommand)
class Cuteqdesigner_internal_MoveTabPageCommand : public qdesigner_internal::MoveTabPageCommand {
public:
  using qdesigner_internal::MoveTabPageCommand::MoveTabPageCommand;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZN12QUndoCommand4redoEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZN12QUndoCommand4undoEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZNK12QUndoCommand2idEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
    if (!std::strcmp(key, "_ZN12QUndoCommand9mergeWithEPKS_")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(undocommand)
    return false;
  }

#if QT_CONFIG(undocommand)
  //  void qdesigner_internal::MoveTabPageCommand::redo()
  void redo() override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_MoveTabPageCommandCall0 call = reinterpret_cast<Cuteqdesigner_internal_MoveTabPageCommandCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::MoveTabPageCommand::redo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  void qdesigner_internal::MoveTabPageCommand::undo()
  void undo() override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_MoveTabPageCommandCall1 call = reinterpret_cast<Cuteqdesigner_internal_MoveTabPageCommandCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::MoveTabPageCommand::undo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  int QUndoCommand::id() const
  int id() const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_MoveTabPageCommandCall2 call = reinterpret_cast<Cuteqdesigner_internal_MoveTabPageCommandCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QUndoCommand::id();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  bool QUndoCommand::mergeWith(const QUndoCommand *other)
  bool mergeWith(const QUndoCommand *other) override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_MoveTabPageCommandCall3 call = reinterpret_cast<Cuteqdesigner_internal_MoveTabPageCommandCall3>(taken[3]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QUndoCommand::mergeWith(other);
  }
#endif  // QT_CONFIG(undocommand)
};

//  qdesigner_internal::MoveTabPageCommand::~MoveTabPageCommand()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18MoveTabPageCommandD1Ev(
    qdesigner_internal::MoveTabPageCommand *self) {
  delete self;
}

//  void qdesigner_internal::MoveTabPageCommand::init(QTabWidget *tabWidget,
//      QWidget *page, const QIcon &icon, const QString &label, int index,
//      int newIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18MoveTabPageCommand4initEP10QTabWidgetP7QWidgetRK5QIconRK7QStringii(
    qdesigner_internal::MoveTabPageCommand *self,
    QTabWidget *tabWidget,
    QWidget *page,
    const QIcon *icon,
    const QString *label,
    int index,
    int newIndex) {
  self->init(tabWidget, page, *icon, *label, index, newIndex);
}

//  void qdesigner_internal::MoveTabPageCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18MoveTabPageCommand4redoEv(
    qdesigner_internal::MoveTabPageCommand *self) {
  self->redo();
}

//  void qdesigner_internal::MoveTabPageCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18MoveTabPageCommand4undoEv(
    qdesigner_internal::MoveTabPageCommand *self) {
  self->undo();
}

//  a Python function taken by a Cuteqdesigner_internal_MoveTabPageCommand,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_MoveTabPageCommand(
    qdesigner_internal::MoveTabPageCommand *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_MoveTabPageCommand *>(self)->take(key, call);
}

//  void qdesigner_internal::MoveTabPageCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal18MoveTabPageCommand4redoEv(
    qdesigner_internal::MoveTabPageCommand *self) {
  self->qdesigner_internal::MoveTabPageCommand::redo();
}

//  void qdesigner_internal::MoveTabPageCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal18MoveTabPageCommand4undoEv(
    qdesigner_internal::MoveTabPageCommand *self) {
  self->qdesigner_internal::MoveTabPageCommand::undo();
}
