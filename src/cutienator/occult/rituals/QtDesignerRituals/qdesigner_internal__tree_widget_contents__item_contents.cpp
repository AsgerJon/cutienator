//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 2430, as _ZN18qdesigner_internal18TreeWidgetContents12ItemContentsC1EPK15QTreeWidgetItemb
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline TreeWidgetContents::ItemContents::ItemContents(const QTreeWidgetItem *item, bool editor) :
    ListContents(item)
{
    static const Qt::ItemFlags defaultFlags = QTreeWidgetItem().flags();

    if (editor) {
        QVariant v = item->data(0, ItemFlagsShadowRole);
        m_itemFlags = v.isValid() ? v.toInt() : -1;
    } else  {
        m_itemFlags = (item->flags() != defaultFlags) ? int(item->flags()) : -1;
    }

    for (int i = 0; i < item->childCount(); i++)
        m_children.append(ItemContents(item->child(i), editor));
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/qdesigner_command.cpp, line 2446, as _ZNK18qdesigner_internal18TreeWidgetContents12ItemContents14createTreeItemEPNS_17DesignerIconCacheEb
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline QTreeWidgetItem *TreeWidgetContents::ItemContents::createTreeItem(DesignerIconCache *iconCache, bool editor) const
{
    QTreeWidgetItem *item = ListContents::createTreeItem(iconCache);

    if (editor)
        item->setFlags(item->flags() | Qt::ItemIsEditable);

    if (m_itemFlags != -1) {
        if (editor)
            item->setData(0, ItemFlagsShadowRole, QVariant::fromValue(m_itemFlags));
        else
            item->setFlags((Qt::ItemFlags)m_itemFlags);
    }

    for (const ItemContents &ic : m_children)
        item->addChild(ic.createTreeItem(iconCache, editor));

    return item;
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  qdesigner_internal::TreeWidgetContents::ItemContents::ItemContents()
extern "C" Q_DECL_EXPORT
qdesigner_internal::TreeWidgetContents::ItemContents *ritual_ZN18qdesigner_internal18TreeWidgetContents12ItemContentsC1Ev() {
  return new qdesigner_internal::TreeWidgetContents::ItemContents();
}

//  qdesigner_internal::TreeWidgetContents::ItemContents::ItemContents(const
//      QTreeWidgetItem *item, bool editor)
extern "C" Q_DECL_EXPORT
qdesigner_internal::TreeWidgetContents::ItemContents *ritual_ZN18qdesigner_internal18TreeWidgetContents12ItemContentsC1EPK15QTreeWidgetItemb(
    const QTreeWidgetItem *item,
    bool editor) {
  return new qdesigner_internal::TreeWidgetContents::ItemContents(
      item,
      editor);
}

//  QTreeWidgetItem *qdesigner_internal::TreeWidgetContents::ItemContents::cr
//      eateTreeItem(DesignerIconCache *iconCache, bool editor) const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK18qdesigner_internal18TreeWidgetContents12ItemContents14createTreeItemEPNS_17DesignerIconCacheEb(
    const qdesigner_internal::TreeWidgetContents::ItemContents *self,
    qdesigner_internal::DesignerIconCache *iconCache,
    bool editor) {
  return self->createTreeItem(iconCache, editor);
}

//  bool operator==(const ItemContents &lhs, const ItemContents &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internaleqERKNS_18TreeWidgetContents12ItemContentsES3_(
    const qdesigner_internal::TreeWidgetContents::ItemContents *lhs,
    const qdesigner_internal::TreeWidgetContents::ItemContents *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const ItemContents &lhs, const ItemContents &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalneERKNS_18TreeWidgetContents12ItemContentsES3_(
    const qdesigner_internal::TreeWidgetContents::ItemContents *lhs,
    const qdesigner_internal::TreeWidgetContents::ItemContents *rhs) {
  return operator!=(*lhs, *rhs);
}

//  qdesigner_internal::TreeWidgetContents::ItemContents::~ItemContents()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18TreeWidgetContents12ItemContentsD1Ev(
    qdesigner_internal::TreeWidgetContents::ItemContents *self) {
  delete self;
}
