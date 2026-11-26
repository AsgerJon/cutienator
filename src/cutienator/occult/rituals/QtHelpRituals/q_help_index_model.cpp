//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/qhelpindexwidget.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the include of
//  <QtTools/qttools-config.h> before the #if, as it defines
//  QT_CONFIG(fullqthelp).
//  Kept as it is when the generator runs again.
#include <QtHelp/qhelp_global.h>
#include <QtTools/qttools-config.h>
#if QT_CONFIG(fullqthelp)
#include <QtHelp/QtHelp>
#include <QtHelp/qhelpindexwidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>

//  const QMetaObject *QHelpIndexModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QHelpIndexModel10metaObjectEv(
    const QHelpIndexModel *self) {
  return self->metaObject();
}

//  void *QHelpIndexModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QHelpIndexModel11qt_metacastEPKc(
    QHelpIndexModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString QHelpIndexModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QHelpIndexModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHelpIndexModel::tr(s, c, n));
}

//  void QHelpIndexModel::createIndexForCurrentFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHelpIndexModel27createIndexForCurrentFilterEv(
    QHelpIndexModel *self) {
  self->createIndexForCurrentFilter();
}

//  void QHelpIndexModel::createIndex(const QString &customFilterName)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHelpIndexModel11createIndexERK7QString(
    QHelpIndexModel *self,
    const QString *customFilterName) {
  self->createIndex(*customFilterName);
}

//  QModelIndex QHelpIndexModel::filter(const QString &filter, const QString
//      &wildcard)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN15QHelpIndexModel6filterERK7QStringS2_(
    QHelpIndexModel *self,
    const QString *filter,
    const QString *wildcard) {
  return new QModelIndex(self->filter(*filter, *wildcard));
}

//  bool QHelpIndexModel::isCreatingIndex() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QHelpIndexModel15isCreatingIndexEv(
    const QHelpIndexModel *self) {
  return self->isCreatingIndex();
}

//  QHelpEngineCore *QHelpIndexModel::helpEngine() const
extern "C" Q_DECL_EXPORT
QHelpEngineCore *ritual_ZNK15QHelpIndexModel10helpEngineEv(
    const QHelpIndexModel *self) {
  return self->helpEngine();
}

//  void QHelpIndexModel::indexCreationStarted()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHelpIndexModel20indexCreationStartedEv(
    QHelpIndexModel *self) {
  self->indexCreationStarted();
}

//  void QHelpIndexModel::indexCreated()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHelpIndexModel12indexCreatedEv(QHelpIndexModel *self) {
  self->indexCreated();
}

//  void QHelpIndexModel::insertIndices()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHelpIndexModel13insertIndicesEv(QHelpIndexModel *self) {
  self->insertIndices();
}

//  QHelpIndexModel::QHelpIndexModel(QHelpEngineCore *helpEngine)
extern "C" Q_DECL_EXPORT
QHelpIndexModel *ritual_ZN15QHelpIndexModelC1EP15QHelpEngineCore(
    QHelpEngineCore *helpEngine) {
  return new QHelpIndexModel(helpEngine);
}

//  QHelpIndexModel::~QHelpIndexModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHelpIndexModelD1Ev(QHelpIndexModel *self) {
  delete self;
}

#endif  // QT_CONFIG(fullqthelp)
