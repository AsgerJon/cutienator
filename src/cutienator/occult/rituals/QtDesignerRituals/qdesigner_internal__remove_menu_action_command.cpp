//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only WITH Qt-GPL-exception-1.0
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 2751, as _ZN18qdesigner_internal17MenuActionCommand10insertMenuEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void MenuActionCommand::insertMenu()
{
    core()->metaDataBase()->add(m_action);
    QMenu *menu = m_action->menu();
    if (m_menuParent && menu->parentWidget() != m_menuParent)
        menu->setParent(m_menuParent);
    core()->metaDataBase()->add(menu);
    m_associatedWidget->insertAction(m_actionBefore, m_action);
    cheapUpdate();
    selectUnmanagedObject(menu);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 2763, as _ZN18qdesigner_internal17MenuActionCommand10removeMenuEv
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void MenuActionCommand::removeMenu()
{
    m_action->menu()->setParent(nullptr);
    QMenu *menu = m_action->menu();
    core()->metaDataBase()->remove(menu);
    menu->setParent(nullptr);
    core()->metaDataBase()->remove(m_action);
    m_associatedWidget->removeAction(m_action);
    cheapUpdate();
    selectUnmanagedObject(m_objectToSelect);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 2729, as _ZN18qdesigner_internal17MenuActionCommandC2ERK7QStringP28QDesignerFormWindowInterface
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline MenuActionCommand::MenuActionCommand(const QString &text, QDesignerFormWindowInterface *formWindow) :
    QDesignerFormWindowCommand(text, formWindow),
    m_action(nullptr),
    m_actionBefore(nullptr),
    m_menuParent(nullptr),
    m_associatedWidget(nullptr),
    m_objectToSelect(nullptr)
{
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 2781, as _ZN18qdesigner_internal23RemoveMenuActionCommandC1EP28QDesignerFormWindowInterface
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline RemoveMenuActionCommand::RemoveMenuActionCommand(QDesignerFormWindowInterface *formWindow) :
    MenuActionCommand(QApplication::translate("Command", "Remove menu"), formWindow)
{
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  A qdesigner_internal::RemoveMenuActionCommand that Python can take functions over in. Every qdesigner_internal::RemoveMenuActionCommand
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_RemoveMenuActionCommandCall0)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef void (*Cuteqdesigner_internal_RemoveMenuActionCommandCall1)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef int (*Cuteqdesigner_internal_RemoveMenuActionCommandCall2)(const void *, int *);
#endif  // QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
typedef bool (*Cuteqdesigner_internal_RemoveMenuActionCommandCall3)(const void *, const QUndoCommand *, int *);
#endif  // QT_CONFIG(undocommand)
class Cuteqdesigner_internal_RemoveMenuActionCommand : public qdesigner_internal::RemoveMenuActionCommand {
public:
  using qdesigner_internal::RemoveMenuActionCommand::RemoveMenuActionCommand;
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
  //  void qdesigner_internal::RemoveMenuActionCommand::redo()
  void redo() override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_RemoveMenuActionCommandCall0 call = reinterpret_cast<Cuteqdesigner_internal_RemoveMenuActionCommandCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::RemoveMenuActionCommand::redo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  void qdesigner_internal::RemoveMenuActionCommand::undo()
  void undo() override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_RemoveMenuActionCommandCall1 call = reinterpret_cast<Cuteqdesigner_internal_RemoveMenuActionCommandCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    qdesigner_internal::RemoveMenuActionCommand::undo();
  }
#endif  // QT_CONFIG(undocommand)

#if QT_CONFIG(undocommand)
  //  int QUndoCommand::id() const
  int id() const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_RemoveMenuActionCommandCall2 call = reinterpret_cast<Cuteqdesigner_internal_RemoveMenuActionCommandCall2>(taken[2]);
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
      Cuteqdesigner_internal_RemoveMenuActionCommandCall3 call = reinterpret_cast<Cuteqdesigner_internal_RemoveMenuActionCommandCall3>(taken[3]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QUndoCommand::mergeWith(other);
  }
#endif  // QT_CONFIG(undocommand)
};

//  qdesigner_internal::RemoveMenuActionCommand::RemoveMenuActionCommand(QDes
//      ignerFormWindowInterface *formWindow)
extern "C" Q_DECL_EXPORT
qdesigner_internal::RemoveMenuActionCommand *ritual_ZN18qdesigner_internal23RemoveMenuActionCommandC1EP28QDesignerFormWindowInterface(
    QDesignerFormWindowInterface *formWindow) {
  return new Cuteqdesigner_internal_RemoveMenuActionCommand(formWindow);
}

//  void qdesigner_internal::RemoveMenuActionCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23RemoveMenuActionCommand4redoEv(
    qdesigner_internal::RemoveMenuActionCommand *self) {
  self->redo();
}

//  void qdesigner_internal::RemoveMenuActionCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23RemoveMenuActionCommand4undoEv(
    qdesigner_internal::RemoveMenuActionCommand *self) {
  self->undo();
}

//  a Python function taken by a
//      Cuteqdesigner_internal_RemoveMenuActionCommand, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_RemoveMenuActionCommand(
    qdesigner_internal::RemoveMenuActionCommand *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_RemoveMenuActionCommand *>(self)->take(key, call);
}

//  void qdesigner_internal::RemoveMenuActionCommand::redo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal23RemoveMenuActionCommand4redoEv(
    qdesigner_internal::RemoveMenuActionCommand *self) {
  self->qdesigner_internal::RemoveMenuActionCommand::redo();
}

//  void qdesigner_internal::RemoveMenuActionCommand::undo()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal23RemoveMenuActionCommand4undoEv(
    qdesigner_internal::RemoveMenuActionCommand *self) {
  self->qdesigner_internal::RemoveMenuActionCommand::undo();
}
