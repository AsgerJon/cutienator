//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/qhelp_global.h, Qt 6.12.0. Changes made here are lost.
#include <QtHelp/qhelp_global.h>
#include <QtCore/qstring.h>

//  QString QHelpGlobal::uniquifyConnectionName(const QString &name, void
//      *pointer)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QHelpGlobal22uniquifyConnectionNameERK7QStringPv(
    const QString *name,
    void *pointer) {
  return new QString(QHelpGlobal::uniquifyConnectionName(*name, pointer));
}

//  QString QHelpGlobal::documentTitle(const QString &content)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QHelpGlobal13documentTitleERK7QString(
    const QString *content) {
  return new QString(QHelpGlobal::documentTitle(*content));
}

//  QHelpGlobal::~QHelpGlobal()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHelpGlobalD1Ev(QHelpGlobal *self) {
  delete self;
}
