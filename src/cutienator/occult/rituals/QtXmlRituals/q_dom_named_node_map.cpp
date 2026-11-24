//  Written by dev_tooling.RitualGenerator from the records of QtXml/qdom.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtXml/qtxmlglobal.h>
#if QT_CONFIG(dom)
#include <QtXml/qdom.h>
#include <QtCore/qstring.h>

//  QDomNamedNodeMap::QDomNamedNodeMap()
extern "C" Q_DECL_EXPORT
QDomNamedNodeMap *ritual_ZN16QDomNamedNodeMapC1Ev() {
  return new QDomNamedNodeMap();
}

//  QDomNamedNodeMap::QDomNamedNodeMap(const QDomNamedNodeMap &namedNodeMap)
extern "C" Q_DECL_EXPORT
QDomNamedNodeMap *ritual_ZN16QDomNamedNodeMapC1ERKS_(
    const QDomNamedNodeMap *namedNodeMap) {
  return new QDomNamedNodeMap(*namedNodeMap);
}

//  bool QDomNamedNodeMap::operator==(const QDomNamedNodeMap &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QDomNamedNodeMapeqERKS_(
    const QDomNamedNodeMap *self,
    const QDomNamedNodeMap *other) {
  return self->operator==(*other);
}

//  bool QDomNamedNodeMap::operator!=(const QDomNamedNodeMap &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QDomNamedNodeMapneERKS_(
    const QDomNamedNodeMap *self,
    const QDomNamedNodeMap *other) {
  return self->operator!=(*other);
}

//  QDomNamedNodeMap::~QDomNamedNodeMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDomNamedNodeMapD1Ev(QDomNamedNodeMap *self) {
  delete self;
}

//  QDomNode QDomNamedNodeMap::namedItem(const QString &name) const
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZNK16QDomNamedNodeMap9namedItemERK7QString(
    const QDomNamedNodeMap *self,
    const QString *name) {
  return new QDomNode(self->namedItem(*name));
}

//  QDomNode QDomNamedNodeMap::setNamedItem(const QDomNode &newNode)
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZN16QDomNamedNodeMap12setNamedItemERK8QDomNode(
    QDomNamedNodeMap *self,
    const QDomNode *newNode) {
  return new QDomNode(self->setNamedItem(*newNode));
}

//  QDomNode QDomNamedNodeMap::removeNamedItem(const QString &name)
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZN16QDomNamedNodeMap15removeNamedItemERK7QString(
    QDomNamedNodeMap *self,
    const QString *name) {
  return new QDomNode(self->removeNamedItem(*name));
}

//  QDomNode QDomNamedNodeMap::item(int index) const
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZNK16QDomNamedNodeMap4itemEi(
    const QDomNamedNodeMap *self,
    int index) {
  return new QDomNode(self->item(index));
}

//  QDomNode QDomNamedNodeMap::namedItemNS(const QString &nsURI, const
//      QString &localName) const
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZNK16QDomNamedNodeMap11namedItemNSERK7QStringS2_(
    const QDomNamedNodeMap *self,
    const QString *nsURI,
    const QString *localName) {
  return new QDomNode(self->namedItemNS(*nsURI, *localName));
}

//  QDomNode QDomNamedNodeMap::setNamedItemNS(const QDomNode &newNode)
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZN16QDomNamedNodeMap14setNamedItemNSERK8QDomNode(
    QDomNamedNodeMap *self,
    const QDomNode *newNode) {
  return new QDomNode(self->setNamedItemNS(*newNode));
}

//  QDomNode QDomNamedNodeMap::removeNamedItemNS(const QString &nsURI, const
//      QString &localName)
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZN16QDomNamedNodeMap17removeNamedItemNSERK7QStringS2_(
    QDomNamedNodeMap *self,
    const QString *nsURI,
    const QString *localName) {
  return new QDomNode(self->removeNamedItemNS(*nsURI, *localName));
}

//  int QDomNamedNodeMap::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QDomNamedNodeMap6lengthEv(const QDomNamedNodeMap *self) {
  return self->length();
}

//  int QDomNamedNodeMap::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QDomNamedNodeMap5countEv(const QDomNamedNodeMap *self) {
  return self->count();
}

//  int QDomNamedNodeMap::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QDomNamedNodeMap4sizeEv(const QDomNamedNodeMap *self) {
  return self->size();
}

//  bool QDomNamedNodeMap::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QDomNamedNodeMap7isEmptyEv(const QDomNamedNodeMap *self) {
  return self->isEmpty();
}

//  bool QDomNamedNodeMap::contains(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QDomNamedNodeMap8containsERK7QString(
    const QDomNamedNodeMap *self,
    const QString *name) {
  return self->contains(*name);
}

//  QDomNamedNodeMap::QDomNamedNodeMap(QDomNamedNodeMapPrivate *a0)
extern "C" Q_DECL_EXPORT
QDomNamedNodeMap *ritual_ZN16QDomNamedNodeMapC1EP23QDomNamedNodeMapPrivate(
    QDomNamedNodeMapPrivate *a0) {
  return new QDomNamedNodeMap(a0);
}

#endif  // QT_CONFIG(dom)
