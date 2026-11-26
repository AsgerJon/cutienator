//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  qdesigner_internal::TableWidgetContents::TableWidgetContents()
extern "C" Q_DECL_EXPORT
qdesigner_internal::TableWidgetContents *ritual_ZN18qdesigner_internal19TableWidgetContentsC1Ev() {
  return new qdesigner_internal::TableWidgetContents();
}

//  void qdesigner_internal::TableWidgetContents::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal19TableWidgetContents5clearEv(
    qdesigner_internal::TableWidgetContents *self) {
  self->clear();
}

//  void qdesigner_internal::TableWidgetContents::fromTableWidget(const
//      QTableWidget *tableWidget, bool editor)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal19TableWidgetContents15fromTableWidgetEPK12QTableWidgetb(
    qdesigner_internal::TableWidgetContents *self,
    const QTableWidget *tableWidget,
    bool editor) {
  self->fromTableWidget(tableWidget, editor);
}

//  void
//      qdesigner_internal::TableWidgetContents::applyToTableWidget(QTableWid
//      get *tableWidget, DesignerIconCache *iconCache, bool editor) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18qdesigner_internal19TableWidgetContents18applyToTableWidgetEP12QTableWidgetPNS_17DesignerIconCacheEb(
    const qdesigner_internal::TableWidgetContents *self,
    QTableWidget *tableWidget,
    qdesigner_internal::DesignerIconCache *iconCache,
    bool editor) {
  self->applyToTableWidget(tableWidget, iconCache, editor);
}

//  bool qdesigner_internal::TableWidgetContents::nonEmpty(const
//      QTableWidgetItem *item, int headerColumn)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal19TableWidgetContents8nonEmptyEPK16QTableWidgetItemi(
    const QTableWidgetItem *item,
    int headerColumn) {
  return qdesigner_internal::TableWidgetContents::nonEmpty(
      item,
      headerColumn);
}

//  QString qdesigner_internal::TableWidgetContents::defaultHeaderText(int i)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal19TableWidgetContents17defaultHeaderTextEi(
    int i) {
  return new QString(
      qdesigner_internal::TableWidgetContents::defaultHeaderText(
          i));
}

//  void qdesigner_internal::TableWidgetContents::insertHeaderItem(const
//      QTableWidgetItem *item, int i, ListContents *header, bool editor)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal19TableWidgetContents16insertHeaderItemEPK16QTableWidgetItemiPNS_12ListContentsEb(
    const QTableWidgetItem *item,
    int i,
    qdesigner_internal::ListContents *header,
    bool editor) {
  qdesigner_internal::TableWidgetContents::insertHeaderItem(
      item,
      i,
      header,
      editor);
}

//  bool operator==(const TableWidgetContents &lhs, const TableWidgetContents
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internaleqERKNS_19TableWidgetContentsES2_(
    const qdesigner_internal::TableWidgetContents *lhs,
    const qdesigner_internal::TableWidgetContents *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const TableWidgetContents &lhs, const TableWidgetContents
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalneERKNS_19TableWidgetContentsES2_(
    const qdesigner_internal::TableWidgetContents *lhs,
    const qdesigner_internal::TableWidgetContents *rhs) {
  return operator!=(*lhs, *rhs);
}

//  qdesigner_internal::TableWidgetContents::~TableWidgetContents()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal19TableWidgetContentsD1Ev(
    qdesigner_internal::TableWidgetContents *self) {
  delete self;
}
