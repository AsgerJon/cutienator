//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfileselector_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qfileselector.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfileselector_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qchar.h>
#include <QtCore/qlist.h>

//  QFileSelector *QFileSelectorPrivate::q_func()
extern "C" Q_DECL_EXPORT
QFileSelector *ritual_ZN20QFileSelectorPrivate6q_funcEv(
    QFileSelectorPrivate *self) {
  return self->q_func();
}

//  const QFileSelector *QFileSelectorPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QFileSelector *ritual_ZNK20QFileSelectorPrivate6q_funcEv(
    const QFileSelectorPrivate *self) {
  return self->q_func();
}

//  void QFileSelectorPrivate::updateSelectors()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFileSelectorPrivate15updateSelectorsEv() {
  QFileSelectorPrivate::updateSelectors();
}

//  QStringList QFileSelectorPrivate::platformSelectors()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN20QFileSelectorPrivate17platformSelectorsEv() {
  return new QList<QString>(QFileSelectorPrivate::platformSelectors());
}

//  void QFileSelectorPrivate::addStatics(const QStringList &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFileSelectorPrivate10addStaticsERK5QListI7QStringE(
    const QList<QString> *a0) {
  QFileSelectorPrivate::addStatics(*a0);
}

//  qsizetype QFileSelectorPrivate::removeStatics(const QStringList &a0)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN20QFileSelectorPrivate13removeStaticsERK5QListI7QStringE(
    const QList<QString> *a0) {
  return QFileSelectorPrivate::removeStatics(*a0);
}

//  QString QFileSelectorPrivate::selectionHelper(const QString &path, const
//      QString &fileName, const QStringList &selectors, QChar indicator)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QFileSelectorPrivate15selectionHelperERK7QStringS2_RK5QListIS0_E5QChar(
    const QString *path,
    const QString *fileName,
    const QList<QString> *selectors,
    const QChar *indicator) {
  return new QString(
      QFileSelectorPrivate::selectionHelper(
          *path,
          *fileName,
          *selectors,
          *indicator));
}

//  QFileSelectorPrivate::QFileSelectorPrivate()
extern "C" Q_DECL_EXPORT
QFileSelectorPrivate *ritual_ZN20QFileSelectorPrivateC1Ev() {
  return new QFileSelectorPrivate();
}

//  QString QFileSelectorPrivate::select(const QString &filePath) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QFileSelectorPrivate6selectERK7QString(
    const QFileSelectorPrivate *self,
    const QString *filePath) {
  return new QString(self->select(*filePath));
}
